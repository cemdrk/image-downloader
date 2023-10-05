from datetime import datetime
from uuid import UUID

from sqlalchemy.orm import Session

from src.db import get_db
from src.models import Download, DownloadStatus


def create_download(session: Session = get_db()) -> Download:
    d = Download()
    session.add(d)
    session.commit()
    session.refresh(d)
    return d


def update_status(
    download_id: UUID, status: str, session: Session = get_db()
) -> Download:
    d = session.query(Download).filter(Download.download_id == download_id).first()
    d.status = status
    if status == DownloadStatus.FINISHED.value:
        d.finished_at = datetime.utcnow()
    session.commit()
    return d


def get_download(download_id: UUID, session: Session = get_db()) -> Download:
    return session.query(Download).filter(Download.download_id == download_id).first()
