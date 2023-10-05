import os
from zipfile import ZipFile

from src.config import settings


class ArchiveException(Exception):
    pass


def generate_zip(
    input_folder: str,
    output_file: str,
    output_folder=settings.DOWNLOAD_PATH,
):
    """
    :param input_folder: Zipped file folder
    :param output_file: Zip file name
    :param output_folder: Folder for saving Zip file
    """
    file_paths = []
    # get file path to be included for creating zip
    for folderName, _, file_names in os.walk(input_folder):
        for f_name in file_names:
            file_path = os.path.join(folderName, f_name)
            file_paths.append(file_path)

    if not file_paths:
        raise ArchiveException("Empty zip")

    with ZipFile(f"{output_folder}/{output_file}.zip", "w") as zipObj:
        for file_path in file_paths:
            base_name = os.path.basename(file_path)
            zipObj.write(file_path, base_name)
