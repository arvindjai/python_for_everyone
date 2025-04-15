import pymongo

myclient = pymongo.MongoClient("mongo://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = {"address": "Mountain 21"}
mycol.delete_one(myquery)


myquery = {"address": {"$regex","^S"}}
x = mycol.delete_many(myquery)
print(x.deleted_count, " documents deleted.")
