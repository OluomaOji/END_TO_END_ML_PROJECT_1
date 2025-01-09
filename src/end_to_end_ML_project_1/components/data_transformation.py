import os
from src.end_to_end_ML_project_1 import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from src.end_to_end_ML_project_1.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self,config: DataTransformationConfig):
        self.config = config

    """
    Different Data Transformation Techniques can be added here such as Scaler, PCA and all.
    Different kinds of EDA in ML cycle can also be performed here before passing the data to the model.
    This data won't go through the whole data transformation process because this is to demonstrate the end to end machine learning learning ETL pipeline.
    This data is already clean and can be used for modeling.
    """

    def train_test_splitting(self):
        data=pd.read_csv(self.config.data_path) 

        #Split the data into training and test datasets.
        train,test = train_test_split(data)
        train.to_csv(os.path.join(self.config.root_dir, 'train_csv'),index= False) 
        test.to_csv(os.path.join(self.config.root_dir, 'test.csv'), index = False)

        logger.info('Splitted data into training and test sets')
        logger.info(train.shape)
        logger.info(test.shape)  
