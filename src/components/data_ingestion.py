import os
import pandas as pd
from src.exception import CustomException
from src.logger import logging
import sys

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_pata:str=os.path.join('artifact','train.csv')
    test_data_pata:str=os.path.join('artifact','test.csv')
    raw_data_pata:str=os.path.join('artifact','data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info('Entering data ingestion component')
        try:
            df=pd.read_csv('notebook\data\stud.csv')
            logging.info('Read the data set as data frame..')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_pata),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_pata,header=True,index=False)
            logging.info('Train test split initiated')

            train_set,test_set=train_test_split(df,test_size=.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_pata,header=True,index=False)
            test_set.to_csv(self.ingestion_config.test_data_pata,header=True,index=False)
            
            logging.info('Ingestion of the data is completed...')

            return (
                self.ingestion_config.train_data_pata,
                self.ingestion_config.test_data_pata
            )
        except Exception as e:
            raise CustomException(e,sys)
        

if __name__=='__main__':
    obj=DataIngestion()
    obj.initiate_data_ingestion()
