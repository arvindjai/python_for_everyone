import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers"
mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
    