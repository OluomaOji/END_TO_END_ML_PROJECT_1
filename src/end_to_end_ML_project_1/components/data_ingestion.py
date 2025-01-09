import os
import urllib.request as request
from src.end_to_end_ML_project_1 import logger
import zipfile
from src.end_to_end_ML_project_1.entity.config_entity import (DataIngestionConfig)


## Component- Data Ingestion
class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config

    # Download the Zip File
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file

            )
            logger.info(f'{filename} download! with following info: \n{headers}')
        else:
            logger.info(f'file already exists of size : ')

    ## Extract The Zip file
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts zip file into data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)