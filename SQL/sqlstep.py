import pandas as pd 
import numpy as np 
import mysql.connector 
from mysql.connector import Error


def create_server_connection(host_name, user_name,user_password):

    connection = None 

    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name, 
            paswd = user_password
        )
    
        print('MySQL Database Connection Successful')

    except Error as err:
        print(f"Error: '{err}'")
    
    return connection

