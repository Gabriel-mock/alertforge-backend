from sqlalchemy.orm import Session
from sqlalchemy.sql import func

from app.models.alert import Alert
from app.core.price_service import get_crypto_price


def check_alerts(db: Session):
    alerts = db.query(Alert).filter(Alert.triggered == False).all()

    for alert in alerts:
        current_price = get_crypto_price(alert.symbol)

        if current_price is None:
            continue

        should_trigger = False

        if alert.condition == "greater_than" and current_price > alert.threshold:
            should_trigger = True

        elif alert.condition == "less_than" and current_price < alert.threshold:
            should_trigger = True

        if should_trigger:
            alert.triggered = True
            alert.triggered_at = func.now()

    db.commit()