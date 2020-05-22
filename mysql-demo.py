import mysql.connector
from tkinter import messagebox


db = mysql.connector.connect(
    host="34.82.239.1",
    user="root",
    passwd="grocery408",
    database="finalproject_pantry2",
)


mycursor = db.cursor()
mycursor.execute("SELECT * FROM Pantry")
myresult = mycursor.fetchall()
print(myresult)

mycursor.execute("CREATE TABLE IF NOT EXISTS BoughtFrom (itemName VARCHAR(64), shopName VARCHAR(255))")
sql = "INSERT INTO BoughtFrom (itemName, shopName) VALUES (%s, %s)"
val = ("Tomato soup", "Trader Joe's")
mycursor.execute(sql, val)
db.commit()

db.close()