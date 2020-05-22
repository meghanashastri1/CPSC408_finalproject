from tkinter import *
import mysql.connector as mysql
import tkinter.messagebox as mbox

class PantryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pantry Database")
        self.root.geometry("1200x750+0+0")
        self.root.config(bg="MediumPurple1")

        ItemID = StringVar()
        ItemName = StringVar()
        BrandName = StringVar()
        FoodGroupID = StringVar()
        Calories = StringVar()
        Quantity = StringVar()
        InPantry = StringVar()

        MainFrame = Frame(self.root, bg="MediumPurple1")
        MainFrame.grid()
        TitleFrame = Frame(MainFrame, bd=2, padx=54, pady=8, bg="Ghost White", relief=RIDGE)
        TitleFrame.pack(side=TOP)

        self.titleLB = Label(TitleFrame, font=('times new roman', 47, 'bold'), text="Pantry Database", bg="Ghost White")
        self.titleLB.grid()

        ButtonFrame =Frame(MainFrame, bd=2, width=1350, height=70, padx=18, pady=10, bg="Ghost White", relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=1, width=1300, height=400, padx=20, pady=20, relief=RIDGE, bg="MediumPurple1")
        DataFrame.pack(side=BOTTOM)

        DataFrameLeft = LabelFrame(DataFrame, bd=1, width=450, height=300, padx=31, pady=3, relief=RIDGE, bg="Ghost White", font=('times new roman', 20, 'bold'), text="Enter grocery item info: \n")
        DataFrameLeft.pack(side=LEFT)

        DataFrameRight = LabelFrame(DataFrame, bd=1, width=1000, height=600, padx=20, relief=RIDGE, bg="Ghost White", font=('times new roman', 20, 'bold'), text="Pantry: \n")
        DataFrameRight.pack(side=RIGHT)

        self.ItemIDlb = Label(TitleFrame, font=('times new roman', 20, 'bold'), text="Item ID: ", bg="Ghost White")
        self.ItemNamelb = Label(TitleFrame, font=('times new roman', 20, 'bold'), text="Item Name: ", bg="Ghost White")
        self.BrandNamelb = Label(TitleFrame, font=('times new roman', 20, 'bold'), text="Brand Name: ", bg="Ghost White")
        self.FoodGrouplb = Label(TitleFrame, font=('times new roman', 20, 'bold'), text="Food Group ID: ", bg="Ghost White")
        self.Calorieslb = Label(TitleFrame, font=('times new roman', 20, 'bold'), text="Calories: ", bg="Ghost White")
        self.lb = Label(TitleFrame, font=('times new roman', 20, 'bold'), text="Item ID: ", bg="Ghost White")




if __name__=='__main__':
    root = Tk()
    application = PantryApp(root)
    root.mainloop()