import mysql.connector
from mysql.connector import Error
import re
import os
import sys
from datetime import date, timedelta

#Creates connection with db, set up to use environment variable for usr pass in future
username = os.environ.get("username")
password = os.environ.get("password")
cnx = mysql.connector.connect(user=username, password=password, host='127.0.0.1', database='logs')
#Repeat functions
#function to execute querys into db from connection
def execute_query(query):
    cursor = cnx.cursor()
    try:
        cursor.execute(query)
        cnx.commit()
        print("Query ran succesfully")
    except Error as err:
        print(f"Error: '{err}'")
#method overloading
def execute_query(query, value):
    cursor = cnx.cursor()
    try:
        cursor.execute(query, value)
        cnx.commit()
        print("Query ran succesfully")
    except Error as err:
        print(f"Error: '{err}'")

#Check for SQL injection and formatting for mac and ip
def safe_mac(mac):
    if any(i in mac for i in "!@#$%&*()'"):                                  #No symbols that can be used maliciously, maybe allcaps/alllower
        return False                                                           #then check that its 0-9, a-e
    for i in mac:
        if not (i.isalnum() or i == ':'):
            return False
    return True
            
def safe_ip(ip):                        #removes single quotes, csv hs them and they are often used in SQL injection 
    part = ip.split('.')
    for i in part:                                       #checks that every value between each . is between 0-255 (standard ipv4)
        if not 0 <= int(i) <= 255:
            return False
    return True

f = open("out.txt")

for x in f:
    parts=re.split()