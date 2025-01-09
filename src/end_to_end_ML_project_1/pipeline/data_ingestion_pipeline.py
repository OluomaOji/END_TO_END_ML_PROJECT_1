from src.end_to_end_ML_project_1.config.configuration import ConfigurationManager
from src.end_to_end_ML_project_1.components.data_ingestion import DataIngestion
from src.end_to_end_ML_project_1 import logger

STAGE_NAME = 'DATA INGESTION STAGE'

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass    
        
    def initiate_data_ingestion(self):
        config=ConfigurationManager()
        data_ingestion_config=config.get_data_ingestion_config()
        data_ingestion=DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == '__main__':
    try: 
        logger.info(f'>>>> stage {STAGE_NAME} started <<<<<<')
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f'>>>> stage {STAGE_NAME} completed <<<<<<')
    except Exception as e:
        logger.exception(e)
        raise e