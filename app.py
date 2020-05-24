from tkinter import *
import mysql.connector
import tkinter.messagebox
import dbQuery

class PantryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pantry Database")
        self.root.geometry("1350x900+0+0")
        self.root.config(bg="MediumPurple1")

        #fields to enter
        ItemID = StringVar()
        ItemName = StringVar()
        BrandName = StringVar()
        Store = StringVar()
        Price = StringVar()
        Weight = StringVar()
        Date = StringVar()
        Expiration = StringVar()
        FoodGroup = StringVar()
        Calories = StringVar()
        InPantry = StringVar()


        #functions called when button is clicked
        def clearData():
            self.ItemIDText.delete(0, END)
            self.ItemNameText.delete(0, END)
            self.BrandNameText.delete(0, END)
            self.StoreText.delete(0, END)
            self.PriceText.delete(0, END)
            self.WeightText.delete(0, END)
            self.purchaseDateText.delete(0, END)
            self.ExpireText.delete(0, END)
            self.FoodGroupText.delete(0, END)
            self.CaloriesText.delete(0, END)
            pantryList.delete(0, END)

        def addRecord():
            item = ItemName.get()
            brand = BrandName.get()
            st = Store.get()
            pr = Price.get()
            w = Weight.get()
            d = Date.get()
            ex = Expiration.get()
            fg = FoodGroup.get()
            cal = Calories.get()
            dbQuery.addItem(item, brand, st, pr, w, d, ex, fg, cal)
            pantryList.delete(0, END)
            pantryList.insert(END, item, brand, st, pr, w, d, ex, fg, cal)

        def searchTable():
            item = ItemName.get()
            dbQuery.searchItem(item)
            pantryList.delete(0, END)
            for myresult in dbQuery.searchItem(item):
                pantryList.insert(END, myresult, str(""))

        def update():
            id = ItemID.get()
            item = ItemName.get()
            dbQuery.updateItem(id, item)
            pantryList.delete(0, END)
            pantryList.insert(id, item)

        def deleteRecord():
            itemID = ItemID.get()
            item = ItemName.get()
            dbQuery.deleteItem(itemID)
            pantryList.delete(0, END)
            pantryList.insert(END, itemID, item)



        def viewByDate():
            pantryList.delete(0, END)
            for myresult in dbQuery.getPantryDates():
                pantryList.insert(END, myresult, str(""))

        def viewByPrice():
            pantryList.delete(0, END)
            for myresult in dbQuery.getPantryPrices():
                pantryList.insert(END, myresult, str(""))

        def exportCSV():
            dbQuery.exportFile()

        def totalCost():
            pantryList.delete(0, END)
            for cost in dbQuery.getCost():
                pantryList.insert(END, cost)

        #build main Frame
        MainFrame = Frame(self.root, bg="MediumPurple1")
        MainFrame.grid()
        TitleFrame = Frame(MainFrame, bd=2, padx=54, pady=8, bg="Ghost White", relief=RIDGE)
        TitleFrame.pack(side=TOP)

        self.titleLB = Label(TitleFrame, font=('times new roman', 47, 'bold'), text="Pantry Database", bg="Ghost White")
        self.titleLB.grid()


        #build Frame for buttons inside DataFrame on bottom of the main fram
        ButtonFrame =Frame(MainFrame, bd=2, width=1300, height=100, padx=18, pady=10, bg="Ghost White", relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)


        #build frame on the bottom meant for buttons
        DataFrame = Frame(MainFrame, bd=1, width=1300, height=400, padx=100, pady=100, relief=RIDGE, bg="MediumPurple1")
        DataFrame.pack(side=BOTTOM)

        #build frame for field entry
        DataFrameLeft = LabelFrame(DataFrame, bd=1, width=1000, height=1000, padx=20, relief=RIDGE, bg="Ghost White", font=('times new roman', 20, 'bold'), text="Enter grocery item info: \n")
        DataFrameLeft.pack(side=LEFT)

        #build frame for listbox that will display results of queries
        DataFrameRight = LabelFrame(DataFrame, bd=1, width=450, height=400, padx=31, pady=3, relief=RIDGE, bg="Ghost White", font=('times new roman', 20, 'bold'), text="Pantry: \n")
        DataFrameRight.pack(side=RIGHT)


        #labels and grids of the entry fields
        self.ItemIDlb = Label(DataFrameLeft, font=('times new roman', 20, 'bold'), text="Item ID: ", padx=2, pady=2, bg="Ghost White")
        self.ItemIDlb.grid(row=0, column=0, sticky=W)
        self.ItemIDText = Entry(DataFrameLeft, font=('times new roman', 20,'bold'), textvariable=ItemID, width=20)
        self.ItemIDText.grid(row=0, column=1, sticky=W)

        self.ItemNamelb = Label(DataFrameLeft, font=('times new roman', 20, 'bold'), text="Item Name: ", padx=2, pady=2, bg="Ghost White")
        self.ItemNamelb.grid(row=1, column=0, sticky=W)
        self.ItemNameText = Entry(DataFrameLeft, font=('times new roman', 20, 'bold'), textvariable=ItemName, width=20)
        self.ItemNameText.grid(row=1, column=1, sticky=W)

        self.BrandNamelb = Label(DataFrameLeft, font=('times new roman', 20, 'bold'), text="Brand Name: ", padx=2, pady=2, bg="Ghost White")
        self.BrandNamelb.grid(row=2, column=0, sticky=W)
        self.BrandNameText = Entry(DataFrameLeft, font=('times new roman', 20, 'bold'), textvariable=BrandName, width=20)
        self.BrandNameText.grid(row=2, column=1, sticky=W)

        self.Storelb = Label(DataFrameLeft, font=('times new roman', 20, 'bold'), text="Purchased From: ", padx=2, pady=2, bg="Ghost White")
        self.Storelb.grid(row=3, column=0, sticky=W)
        self.StoreText = Entry(DataFrameLeft, font=('times new roman', 20, 'bold'), textvariable=Store, width=20)
        self.StoreText.grid(row=3, column=1, sticky=W)

        self.Pricelb = Label(DataFrameLeft, font=('times new roman', 20, 'bold'), text="Price: ", padx=2, pady=2, bg="Ghost White")
        self.Pricelb.grid(row=4, column=0, sticky=W)
        self.PriceText = Entry(DataFrameLeft, font=('times new roman', 20, 'bold'), textvariable=Price, width=20)
        self.PriceText.grid(row=4, column=1, sticky=W)

        self.Weightlb = Label(DataFrameLeft, font=('times new roman', 20, 'bold'), text="Weight in grams: ", padx=2, pady=2, bg="Ghost White")
        self.Weightlb.grid(row=5, column=0, sticky=W)
        self.WeightText = Entry(DataFrameLeft, font=('times new roman', 20, 'bold'), textvariable=Weight, width=20)
        self.WeightText.grid(row=5, column=1, sticky=W)

        self.purchaseDatelb = Label(DataFrameLeft, font=('times new roman', 20, 'bold'), text="Date Purchased: ", padx=2, pady=2, bg="Ghost White")
        self.purchaseDatelb.grid(row=6, column=0, sticky=W)
        self.purchaseDateText = Entry(DataFrameLeft, font=('times new roman', 20, 'bold'), textvariable=Date, width=20)
        self.purchaseDateText.grid(row=6, column=1, sticky=W)

        self.Expirelb = Label(DataFrameLeft, font=('times new roman', 20, 'bold'), text="Expiration Date: ", padx=2, pady=2, bg="Ghost White")
        self.Expirelb.grid(row=7, column=0, sticky=W)
        self.ExpireText = Entry(DataFrameLeft, font=('times new roman', 20, 'bold'), textvariable=Expiration, width=20)
        self.ExpireText.grid(row=7, column=1, sticky=W)

        self.FoodGrouplb = Label(DataFrameLeft, font=('times new roman', 20, 'bold'), text="Food group/description: ", padx=2, pady=2, bg="Ghost White")
        self.FoodGrouplb.grid(row=8, column=0, sticky=W)
        self.FoodGroupText = Entry(DataFrameLeft, font=('times new roman', 20, 'bold'), textvariable=FoodGroup, width=20)
        self.FoodGroupText.grid(row=8, column=1, sticky=W)

        self.Calorieslb = Label(DataFrameLeft, font=('times new roman', 20, 'bold'), text="Calories: ", padx=2,pady=2, bg="Ghost White")
        self.Calorieslb.grid(row=9, column=0, sticky=W)
        self.CaloriesText = Entry(DataFrameLeft, font=('times new roman', 20, 'bold'), textvariable=Calories, width=20)
        self.CaloriesText.grid(row=9, column=1, sticky=W)


        #list of Pantry table
        scrollbar = Scrollbar(DataFrameRight)
        scrollbar.grid(row=0, column=1, sticky='ns')

        pantryList = Listbox(DataFrameRight, width=80, height=30, font=('times new roman', 14, 'bold'), yscrollcommand=scrollbar.set)
        pantryList.grid(row=0, column=0, padx=8)
        scrollbar.config(command = pantryList.yview)

        #Create buttons in buttonframe
        self.addButton = Button(ButtonFrame, text="Add", font=('times new roman', 14, 'bold'), height=1, width=10, bd=1, command=addRecord)
        self.addButton.grid(row=0, column=0)

        self.deleteButton = Button(ButtonFrame, text="Delete", font=('times new roman', 14, 'bold'), height=1, width=10, bd=1, command=deleteRecord)
        self.deleteButton.grid(row=0, column=1)

        self.viewDateButton = Button(ButtonFrame, text="View data with key dates", font=('times new roman', 14, 'bold'), height=1, width=10, bd=1, command=viewByDate)
        self.viewDateButton.grid(row=0, column=2)

        self.viewPriceButton = Button(ButtonFrame, text="View data with prices", font=('times new roman', 14, 'bold'), height=1, width=10, bd=1, command=viewByPrice)
        self.viewPriceButton.grid(row=0, column=3)

        self.updateButton = Button(ButtonFrame, text="Update", font=('times new roman', 14, 'bold'), height=1, width=10, bd=1, command=update)
        self.updateButton.grid(row=0, column=4)

        self.SearchButton = Button(ButtonFrame, text="Search", font=('times new roman', 14, 'bold'), height=1, width=10, bd=1, command=searchTable)
        self.SearchButton.grid(row=0, column=5)

        self.csvButton = Button(ButtonFrame, text="CSV report", font=('times new roman', 14, 'bold'), height=1, width=10, bd=1, comman=exportCSV)
        self.csvButton.grid(row=0, column=6)

        self.clearButton = Button(ButtonFrame, text="Clear entry", font=('times new roman', 14, 'bold'), height=1, width=10, bd=1, command=clearData)
        self.clearButton.grid(row=0, column=7)

        self.costButton = Button(ButtonFrame, text="Total Cost", font=('times new roman', 14, 'bold'), height=1, width=10, bd=1, command=totalCost)
        self.costButton.grid(row=0, column=8)



#build app with main loop
if __name__=='__main__':
    root = Tk()
    application = PantryApp(root)
    root.mainloop()