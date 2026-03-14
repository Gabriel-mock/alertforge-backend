from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_user
from app.models.alert import Alert
from app.models.user import User
from app.schemas.alert import AlertCreate, AlertResponse
from app.core.alert_checker import check_alerts

router = APIRouter()

@router.post("/alerts", response_model=AlertResponse)
def create_alert(
    alert: AlertCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_alert = Alert(
        user_id=current_user.id,
        symbol=alert.symbol,
        condition=alert.condition,
        threshold=alert.threshold
    )

    db.add(new_alert)
    db.commit()
    db.refresh(new_alert)
    return new_alert

@router.get("/alerts", response_model=list[AlertResponse])
def get_alerts(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    alerts = db.query(Alert).filter(Alert.user_id == current_user.id).all()
    return alerts

@router.delete("/alerts/{alert_id}")
def delete_alert(
    alert_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    alert = db.query(Alert).filter(Alert.id == alert_id).first()

    if not alert:
        raise HTTPException(status_code=404, detail="Alert not found")

    if alert.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")

    db.delete(alert)
    db.commit()

    return {"message": "Alert deleted"}

@router.post("/alerts/check")
def run_alert_check(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    check_alerts(db)
    return {"message": "Alert check completed"}