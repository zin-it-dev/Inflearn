from sqlalchemy import Column, Integer, DateTime
from datetime import datetime, timezone


class TimestampMixin:
    id = Column(Integer, primary_key=True, autoincrement=True)
    date_created = Column(DateTime, default=datetime.now(timezone.utc))
    date_updated = Column(
        DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc)
    )
