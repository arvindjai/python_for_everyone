import mysql.connection

mydb = mysql.connection.connect(
    host = "localhost",
    user = "username",
    password = "password"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE mydatabase")

mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)
