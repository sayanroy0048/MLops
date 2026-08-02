from src.Mlproject.logger import logging
from src.Mlproject.exception import CustomException
from src.Mlproject.components.data_ingestion import data
from src.Mlproject.utils import get_data
from src.Mlproject.components.data_ingestion import data,dataingesionConfig
import sys


if __name__=="__main__":
  try:
    ob = data()
    data_ingestion_config = ob.initiate_data_ingestion()
    print(data_ingestion_config)
  except Exception as e:
    raise CustomException(e,sys)
  