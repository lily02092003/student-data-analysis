import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transformation import DataTransformationConfig
from src.components.data_transformation import DataTransformation
@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts',"train.csv")
    test_data_path: str = os.path.join('artifacts', "test.csv")
    raw_data_path: str = os.path.join('artifacts', "data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
    def initiate_data_ingestion(self):
        logging.info("ENTERED THE DATA INGESTION METHOD")
        try:
                df=pd.read_csv('notebook/data/StudentsPerformance.csv')
                logging.info('DATA IS READ AS DATAFRAME')
                os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

                df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
                x_train, x_test = train_test_split(df,test_size=0.2, random_state=42)
                logging.info("Train Test Split Initiated")
                x_train.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
                x_test.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
                logging.info("Train Test Split Completed")
                return (
                    self.ingestion_config.train_data_path,
                    self.ingestion_config.test_data_path
                )
        except Exception as e:
            raise CustomException(e,sys)
if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    data_transformation.initiate_data_transformation(train_data,test_data)