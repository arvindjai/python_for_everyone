import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")  # Create connection

# Create Database
mydb = myclient["mydatabase"]   # similar to CREATE DATABASE in SQL

# list database
print(myclient.list_database_names())

# check database exists by name
dblist = myclient.list_database_names()
if "mydatabase" in dblist:
    print("Database Exist")
else:
    print("Database not Exist")
