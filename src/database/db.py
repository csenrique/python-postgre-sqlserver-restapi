#import psycopg2 
#from psycopg2 import DatabaseError
import pyodbc
from pyodbc import DatabaseError

from decouple import config

def get_connection():
    try:
        # return psycopg2.connect(
        #     host=config('PGSQL_HOST'),
        #     user=config('PGSQL_USER'),
        #     password=config('PGSQL_PASSWORD'),
        #     database=config('PGSQL_DATABASE')
        # ) 

        return pyodbc.connect('DRIVER={SQL Server};'+f'SERVER={config("SQL_HOST")};DATABASE={config("SQL_DATABASE")};UID={config("SQL_USER")};PWD={config("SQL_PASSWORD")}')

    except DatabaseError as ex:
        raise ex 


