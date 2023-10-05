import os
from uuid import UUID

from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from src.config import settings
from src.db import get_db
from src.schemas import DownloadGetResponse, DownloadRequest, DownloadResponse
from src.services.download import create_download, get_download
from src.tasks import download_and_zip

router = APIRouter()


@router.post("/downloads", response_model=DownloadResponse)
async def start_downloading_images(
    request: DownloadRequest,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
):
    download_record = create_download(db)
    background_tasks.add_task(
        download_and_zip, request.url, download_record.download_id
    )
    return download_record


@router.get("/downloads/{download_id}/status", response_model=DownloadGetResponse)
async def get_download_status(download_id: UUID, db: Session = Depends(get_db)):
    return get_download(download_id=download_id, session=db)


@router.get("/downloads/{download_id}", response_class=FileResponse)
async def download_images(download_id: UUID):
    file_path = f"{settings.DOWNLOAD_PATH}/{download_id}.zip"
    # check if file exists
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File Not Found")
    return FileResponse(file_path)
