import os
import sys
from src.Mlproject.exception import CustomException
from src.Mlproject.logger import logging
import pandas as pd
import numpy as np
from dotenv import load_dotenv 
import pymysql


load_dotenv()


host=os.getenv("host")
username=os.getenv("user")
password=os.getenv("password")
database=os.getenv("database")



def db_connection():
    try:
        conn = pymysql.connect(
            host=host,
            user=username,
            password=password,
            database=database,
            ssl_disabled=True
        )


        logging.info("Connection has been established",conn)


        return conn

    except Exception as e:
        raise CustomException(e,sys)
    


def get_data():

   try:
        conn =  db_connection()
        df = pd.read_sql_query("SELECT * FROM heart_disease",conn)
        print(df.head())
        return df
   
   except Exception as e:
       raise CustomException(e,sys)