import pymongo

conn = pymongo.MongoClient("mongo://localhost:27017/")

mydb = conn["mydatabase"]

# Create a collection called "customers"
mycol = mydb["customers"]

# Return a list of all collections in your database
print(mydb.list_collection_names())

# Check if the "customers" collection exists
collist = mydb.list_collection_names()
if "mycol" in collist:
    print("Collection Exists")

    