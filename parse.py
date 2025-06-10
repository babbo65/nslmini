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

with open(file, 'r') as f:
    content = f.read()

content=content.replace('\r\n', '\n')

tree = ET.ElementTree(ET.fromstring(content))
root = tree.getroot()

#Searhes for and grabs timestamp
time_location=root.find('./runstats/finished')
time=time_location.attrib['timestr']

def logdata(child):
    if element.tag == "host":
        for addr in root.findall(".//address"):
            if addr.attrib.get("addrtype") == "ipv4":
                addr.attrib.get addr
            elif addr.attrib.get("addrtype") == "mac":
                addr.tag = "mac_address"




        #Once it locates port info, check if that ip relative to time is already there and update
        #Else make new entry
        check_if_exists = "SELECT COUNT(*) FROM masscan_report WHERE ip=%s AND time=%s"
        check_values = (ip, time)
        check=execute_query(check_if_exists, check_values)
                if check[0] > 0:
                    query = f"UPDATE  masscan_report SET `port_{port}`=1 WHERE ip=%s AND time=%s"
                    values=(ip, time)
                    execute_query(query, values)
                else:
                    query = f"INSERT INTO masscan_report (ip, time, `port_{port}`) VALUES (%s, %s, %s)"
                    values = (ip, time, 1)
                    execute_query(query, values)
    for child in element:           #Since file is formatted as tree uses recusrion to dive into tree
        logdata(child, time)



logdata(root)
cnx.close()