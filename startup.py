import mysql.connector
from mysql.connector import Error
import os

#Creates connection with db, set up to use environment variable for usr pass in future
#automate building of database and user account/perms
username = os.environ.get("username")
password = os.environ.get("password")
cnx = mysql.connector.connect(user=username, password=password, host='127.0.0.1', database='nslmini')

#function to execute querys into db from connection
def execute_query(query):
    cursor = cnx.cursor()
    try:
        cursor.execute(query)
        cnx.commit()
        print("Query ran succesfully")
    except Error as err:
        print(f"Error: '{err}'")
