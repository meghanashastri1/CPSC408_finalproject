import csv

import mysql.connector


#query to view pantry table by its purcahse and expiration dates
def getPantryDates():
    db = mysql.connector.connect(host="34.82.21.186", user="root", passwd="grocery408", database="finalproject_pantry2",)
    mycursor = db.cursor()
    try:
        mycursor.execute("Select * From Pantry NATURAL JOIN KeyDates NATURAL JOIN PurchasedFrom WHERE InPantry = 1")
        myresult = mycursor.fetchall()
    except:
        db.rollback()
    db.close()
    return myresult

#query to view pantry table by its prices
def getPantryPrices():
    db = mysql.connector.connect(host="34.82.21.186", user="root", passwd="grocery408", database="finalproject_pantry2",)
    mycursor = db.cursor()
    try:
        mycursor.execute("Select * From Pantry NATURAL JOIN Prices NATURAL JOIN PurchasedFrom WHERE InPantry = 1")
        myresult = mycursor.fetchall()
    except:
        db.rollback()
    db.close()
    return myresult

#query to add new item in all tables, must use all fields
def addItem(itemName, brandName, store, price, weight, date, expiration, FoodGroup, Calories):
    db = mysql.connector.connect(host="34.82.21.186", user="root", passwd="grocery408", database="finalproject_pantry2",)
    mycursor = db.cursor()
    try:
        #use multiple insert functions to insert into multiple tables
        sql1 = "INSERT INTO Pantry (ItemName, BrandName, FG_Description, Calories, InPantry) VALUES (%s, %s, %s, %s, 1)"
        val1 = (itemName, brandName, FoodGroup, Calories)
        mycursor.execute(sql1, val1)
        db.commit()

        #LAST_INSERT_ID() will update child tables according to the ItemID of the item insert in the Pantry table
        sql2 = "Insert INTO Prices(ItemID, Price) VALUES (LAST_INSERT_ID(), %s)"
        val2 = price
        mycursor.execute(sql2, val2)
        db.commit()

        sql3 = "INSERT INTO KeyDates(ItemID, DatePurchased, ExpirationDate) VALUES (LAST_INSERT_ID(), %s, %s)"
        val3 = (date, expiration)
        mycursor.execute(sql3, val3)
        db.commit()

        sql4 = "INSERT INTO Weight(ItemID, NetWeightGrams) VALUES (LAST_INSERT_ID(), %s)"
        val4 = weight
        mycursor.execute(sql4, val4)
        db.commit()


        sql5 = "INSERT INTO PurchasedFrom(ItemID, StoreName) VALUES (LAST_INSERT_ID(), %s)"
        val5 = (store)
        mycursor.execute(sql5, val5)
        db.commit()
    except:
        db.rollback()
    db.close()

#soft delete
def deleteItem(itemID):
    db = mysql.connector.connect(host="34.82.21.186", user="root", passwd="grocery408", database="finalproject_pantry2",)
    mycursor = db.cursor()
    try:
        sql = "UPDATE Pantry SET InPantry = 0 WHERE ItemID = %s"
        val = itemID
        mycursor.execute(sql, (val,))
        db.commit()
    except:
        db.rollback()
    db.close()

#search item by its name
def searchItem(itemName):
    db = mysql.connector.connect(host="34.82.21.186", user="root", passwd="grocery408", database="finalproject_pantry2", )
    mycursor = db.cursor()
    try:
        sql = "SELECT * FROM Pantry WHERE ItemName LIKE %s AND InPantry = 1"
        val = itemName
        mycursor.execute(sql, (val,))
        myresult = mycursor.fetchall()
    except:
        db.rollback()
    db.close()
    return myresult

#update item name according to its ID
def updateItem(itemID, itemName):
    db = mysql.connector.connect(host="34.82.21.186", user="root", passwd="grocery408", database="finalproject_pantry2", )
    mycursor = db.cursor()
    try:
        sql = "UPDATE Pantry SET ItemID = %s AND ItemName = %s WHERE ItemID = %s AND InPantry =1"
        val = itemID, itemName
        mycursor.execute(sql, (val,))
        db.commit()
    except:
        db.rollback()
    db.close()

#export Pantry table to a csv file
def exportFile():
    db = mysql.connector.connect(host="34.82.21.186", user="root", passwd="grocery408", database="finalproject_pantry2", )
    mycursor = db.cursor()
    try:
        mycursor.execute("SELECT ItemID, ItemName, BrandName, FG_Description, Calories FROM Pantry WHERE InPantry = 1 ")
        myresult = mycursor.fetchall()
        attributes = [i[0] for i in mycursor.description]
        fileWriter = open('Pantry.csv', 'w')
        file = csv.writer(fileWriter, lineterminator = '\n')
        #include attribute names of the Pantry
        file.writerow(attributes)
        file.writerow(myresult)
        fileWriter.close()
    except:
        db.rollback()
    db.close()

#aggregation clause that will find cost of all items in Pantry by taking the sum of the Prices table
def getCost():
    db = mysql.connector.connect(host="34.82.21.186", user="root", passwd="grocery408", database="finalproject_pantry2", )
    mycursor = db.cursor()
    try:
        mycursor.execute("SELECT SUM(Price) FROM Prices")
        cost = mycursor.fetchall()
        db.commit()
    except:
        db.rollback()
    db.close()
    return cost
