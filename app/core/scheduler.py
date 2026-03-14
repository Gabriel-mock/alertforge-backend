from apscheduler.schedulers.background import BackgroundScheduler
from app.core.database import SessionLocal
from app.core.alert_checker import check_alerts


def run_alert_worker():
    db = SessionLocal()
    try:
        check_alerts(db)
    finally:
        db.close()


def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(run_alert_worker, "interval", seconds=30)
    scheduler.start()