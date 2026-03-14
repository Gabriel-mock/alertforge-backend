from fastapi import FastAPI
from app.core.database import Base, engine
from app.models.user import User
from app.models.alert import Alert
from app.routers.auth import router as auth_router
from app.routers.alerts import router as alerts_router
from app.core.scheduler import start_scheduler


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)
app.include_router(alerts_router)

start_scheduler()

@app.get("/")
def root():
    return {"message": "AlertForge API running"}