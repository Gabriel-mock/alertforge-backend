from datetime import datetime
from pydantic import BaseModel


class AlertCreate(BaseModel):
    symbol: str
    condition: str
    threshold: float


class AlertResponse(BaseModel):
    id: int
    user_id: int
    symbol: str
    condition: str
    threshold: float
    triggered: bool
    triggered_at: datetime | None = None

    class Config:
        from_attributes = True