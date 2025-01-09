from src.end_to_end_ML_project_1.config.configuration import ConfigurationManager
from src.end_to_end_ML_project_1.components.data_validation import DataValidation
from src.end_to_end_ML_project_1 import logger

STAGE_NAME = 'DATA VALIDATION STAGE'

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_validation(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()


if __name__ == '__main__':
    try:
        logger.info(f'>>>>> stage {STAGE_NAME} started <<<<<')
        obj = DataValidationTrainingPipeline()
        obj.initiate_data_validation()
        logger.info(f'>>>>> stage {STAGE_NAME} completed <<<<<\n\nx============x ')
    
    except Exception as e:
        logger.exception(e)
        raise e