import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="abc"
)

mycursor = mydb.cursor()

a=input("enter the name")
b=input("enter the address")


sql = "INSERT INTO st (name, address) VALUES (%s, %s)"
val = (a,b)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

mycursor.execute("select * from st")

res=mycursor.fetchall()

for x in res:
    print(x)

