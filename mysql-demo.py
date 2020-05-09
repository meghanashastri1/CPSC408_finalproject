import mysql.connector

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

db.close()