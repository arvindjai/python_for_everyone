import pymongo

myclient = pymongo.MongoClient("mongo://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

# Ex.1 - returns the first occurrence in the selection
x = mycol.find_one() 
print(x)

# Ex.2 - Return all documents in the "customers" collection.
for x in mycol.find():   # find() --> SELECT * in MYSQL
    print(x)


# Sort 
mydoc = mycol.find().sort("name")
mydoc = mycol.find().sort("name", -1)  # sort by Descending order 

for x in mydoc:
  print(x)

