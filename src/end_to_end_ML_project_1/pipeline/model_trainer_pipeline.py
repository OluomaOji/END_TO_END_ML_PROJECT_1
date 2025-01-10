from src.end_to_end_ML_project_1.config.configuration import ConfigurationManager
from src.end_to_end_ML_project_1.components.model_training import ModelTrainer
from src.end_to_end_ML_project_1 import logger


STAGE_NAME = 'MODEL TRAINING STAGE'

class ModelTrainerPipeline:
    def __init__(self):
        pass    
        
    def initiate_model_trainer(self):
        config=ConfigurationManager()
        model_trainer_config=config.get_model_trainer_config()
        model_trainer=ModelTrainer(config=model_trainer_config)
        model_trainer.train()


if __name__ == '__main__':
    try: 
        logger.info(f'>>>> stage {STAGE_NAME} started <<<<<<')
        obj = ModelTrainerPipeline()
        obj.initiate_model_trainer()
        logger.info(f'>>>> stage {STAGE_NAME} completed <<<<<<')
    except Exception as e:
        logger.exception(e)
        raise e