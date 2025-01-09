from src.end_to_end_ML_project_1.config.configuration import ConfigurationManager
from src.end_to_end_ML_project_1.components.data_transformation import DataTransformation
from src.end_to_end_ML_project_1 import logger
from pathlib import Path

STAGE_NAME = 'DATA TRANSFORMATION STAGE'

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass    
        
    def initiate_data_transformation(self):
        try:
            with open(Path('artifacts/data_validation/status.txt'),'r') as f:
                status=f.read().split(" ")[-1]
            if status=="True":
                config=ConfigurationManager()
                data_transformation_config=config.get_data_transformation_config()
                data_transformation=DataTransformation(config=data_transformation_config)
                data_transformation.train_test_splitting()
            else:
                raise Exception('Your data is not valid')    
        except Exception as e:
            print(e)


if __name__ == '__main__':
    try: 
        logger.info(f'>>>> stage {STAGE_NAME} started <<<<<<')
        obj = DataTransformationTrainingPipeline()
        obj.initiate_data_transformation()
        logger.info(f'>>>> stage {STAGE_NAME} completed <<<<<<')
    except Exception as e:
        logger.exception(e)
        raise e