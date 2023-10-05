import enum
import uuid
from datetime import datetime

from sqlalchemy import Column, DateTime, String
from sqlalchemy.dialects.postgresql import UUID

from src.db import Base


class DownloadStatus(enum.Enum):
    FINISHED = "FINISHED"
    PROCESSING = "PROCESSING"
    ERROR = "ERROR"


class Download(Base):
    __tablename__ = "downloads"
    download_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    started_at = Column(DateTime, default=datetime.utcnow)
    finished_at = Column(DateTime)
    status = Column(String, nullable=False, default=DownloadStatus.PROCESSING.value)
    # alembic autogenerate not working with postgre enum
    # https://github.com/sqlalchemy/alembic/issues/278
