from sqlalchemy import Column, String, DateTime, JSON, Integer
from app.db.session import Base
from datetime import datetime, timezone
import uuid

class UserEvent(Base):
    __tablename__ = "user_events"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, index=True)  # Anon id
    query = Column(String)
    clicked_place_id = Column(String, index=True)
    timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    location_cluster = Column(String)
