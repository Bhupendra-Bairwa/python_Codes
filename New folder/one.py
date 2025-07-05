import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="abc"
)

mycursor = mydb.cursor()



mycursor.execute("select * from st")

res=mycursor.fetchone()

print(res)

