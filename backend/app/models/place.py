from sqlalchemy import Column, String, Float, Boolean, JSON, DateTime, Integer
from geoalchemy2 import Geometry
from app.db.session import Base
from datetime import datetime, timezone

class Place(Base):
    __tablename__ = "places"
    
    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    lat = Column(Float, nullable=False)
    lon = Column(Float, nullable=False)
    location = Column(Geometry('POINT'))
    category = Column(String, index=True)
    rating = Column(Float, default=0.0)
    open_hours = Column(JSON)
    source = Column(String)  # e.g., "osm", "user"
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

class PlaceMetric(Base):
    __tablename__ = "place_metrics"
    
    place_id = Column(String, primary_key=True, index=True)
    impressions = Column(Integer, default=0)
    clicks = Column(Integer, default=0)
    ctr = Column(Float, default=0.0)
    last_updated = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
