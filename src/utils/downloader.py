import os

import aiohttp

from src.config import settings


async def download(
    urls: [str],
    output_folder: str = settings.DOWNLOAD_PATH,
    download_limit: int = settings.DOWNLOAD_LIMIT,
):
    """
    :param urls: URL of the resource to download
    :param output_folder: Downloaded resource folder
    :param download_limit: Limit for downloading
    """
    # create folder if not exists
    os.makedirs(output_folder, exist_ok=True)

    async with aiohttp.ClientSession() as session:
        for url in urls[:download_limit]:
            output_file_name = url.split("/")[-1]
            async with session.get(url) as resp:
                resp.raise_for_status()
                with open(f"{output_folder}/{output_file_name}", mode="wb") as f:
                    f.write(await resp.read())
