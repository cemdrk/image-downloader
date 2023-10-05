import logging
from uuid import UUID

from pydantic import HttpUrl

from src.config import settings
from src.models import DownloadStatus
from src.services.download import update_status
from src.utils.archiver import generate_zip
from src.utils.downloader import download
from src.utils.scraper import get_image_urls

logger = logging.getLogger(__name__)


async def download_and_zip(url: HttpUrl, download_id: UUID):
    """
    :param url: URL of the website to scrape
    :param download_id: Unique id for download process
    """
    download_folder = f"{settings.DOWNLOAD_PATH}/images/{download_id}"

    try:
        img_urls = await get_image_urls(url)
        await download(img_urls, output_folder=download_folder)
        generate_zip(input_folder=download_folder, output_file=download_id)
    except Exception as e:
        logger.error(e)
        update_status(download_id=download_id, status=DownloadStatus.ERROR.value)
    else:
        update_status(download_id=download_id, status=DownloadStatus.FINISHED.value)
