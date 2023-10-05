from fastapi import FastAPI

from src.api import api_router

app = FastAPI(title="Image Downloader")

app.include_router(api_router)
