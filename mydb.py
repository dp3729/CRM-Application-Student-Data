#Install MySql on the computer
#pip install mysql
#pip install mysql-connector
#pip install mysql-connector-python


import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "password123"
)


# Prepare a cursor project
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")
