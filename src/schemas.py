from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field, HttpUrl, root_validator

from src.config import settings


class DownloadRequest(BaseModel):
    url: HttpUrl = Field(example="https://webscraper.io/test-sites")


class DownloadGetResponse(BaseModel):
    download_id: UUID
    started_at: datetime
    finished_at: Optional[datetime]
    status: str
    download_url: Optional[str]

    @root_validator
    def compute_download_url(cls, values) -> str:
        if values["download_url"] is None:
            download_url = f"{settings.HOST}/downloads/{values['download_id']}"
            values["download_url"] = download_url
        return values

    class Config:
        orm_mode = True


class DownloadResponse(BaseModel):
    download_id: UUID

    class Config:
        orm_mode = True
