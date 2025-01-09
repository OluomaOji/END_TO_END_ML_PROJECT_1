from src.end_to_end_ML_project_1 import logger
from src.end_to_end_ML_project_1.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.end_to_end_ML_project_1.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.end_to_end_ML_project_1.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline

STAGE_NAME = 'DATA INGESTION STAGE'
try:
    logger.info(f'>>>>>> stage {STAGE_NAME} started <<<<<<')
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f'>>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx======x')
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = 'DATA VALIDATION STAGE'
try:
    logger.info(f'>>>>> stage {STAGE_NAME} started <<<<<')
    data_validation = DataValidationTrainingPipeline()
    data_validation.initiate_data_validation()
    logger.info(f'>>>>> stage {STAGE_NAME} completed <<<<<\n\nx============x ')   
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'DATA TRANSFORMATION STAGE'
try:
    logger.info(f'>>>>> stage {STAGE_NAME} started <<<<<')
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.initiate_data_transformation()
    logger.info(f'>>>>> stage {STAGE_NAME} completed <<<<<\n\nx============x ')    
except Exception as e:
    logger.exception(e)
    raise e