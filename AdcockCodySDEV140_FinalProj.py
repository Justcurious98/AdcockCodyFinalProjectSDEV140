"""
Author:  Cody Adcock
Date written: 07/23/23
Assignment:   Final Project
Short Desc:   An application to help navigate personal finances. "PennyPilot"
"""


import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

# Global variables
mainMenu = None
expenseWindow = None
viewExpensesWindow = None
dateEntry = None
amountEntry = None
categoryEntry = None
descriptionEntry = None
expensesText = None
welcomeLabel = None
expenseList = []

# Function to be executed when the button is clicked
def startTracking():
    date = dateEntry.get()
    amount = amountEntry.get()
    category = categoryEntry.get()
    description = descriptionEntry.get()

    # Input validation
    if not date or not amount or not category or not description:
        messagebox.showerror("Input Error", "All fields are required.")
        return

    try:
        float(amount)
    except ValueError:
        messagebox.showerror("Input Error", "Amount should be a number.")
        return

    expense = f"{date} | {amount} | {category} | {description}"
    expenseList.append(expense)
    welcomeLabel.config(text="Expense saved successfully!") 

def goToExpenseWindow():
    # Hide the mainMenu window
    mainMenu.withdraw()

    # Show the expenseWindow
    expenseWindow.deiconify()

def goToViewExpensesWindow():
    # Hide the mainMenu window
    mainMenu.withdraw()

    # Show the viewExpensesWindow
    viewExpensesWindow.deiconify()

    # Clear the text box
    expensesText.delete('1.0', tk.END)

    # Insert all expenses into the text box
    expensesText.insert(tk.END, "\n".join(expenseList))

def goToMainMenuFromExpenseWindow():
    # Hide the expenseWindow
    expenseWindow.withdraw()

    # Show the main menu again
    mainMenu.deiconify()

def goToMainMenuFromViewExpensesWindow():
    # Hide the viewExpensesWindow
    viewExpensesWindow.withdraw()

    # Show the main menu again
    mainMenu.deiconify()

def showAbout():
    messagebox.showinfo("About PennyPilot", "PennyPilot is a personal finance tracking application. It helps you navigate your financial journey.")

# Create a tkinter instance for the main menu window
mainMenu = tk.Tk()  
mainMenu.title('PennyPilot: Main Menu')

# Create the image
mainMenu.budgetImage = ImageTk.PhotoImage(Image.open("budgetImage.png"))

# Create a label for the image and pack it
imageLabel = tk.Label(mainMenu, image=mainMenu.budgetImage)
imageLabel.pack()

# Create main menu buttons
expenseButton = tk.Button(mainMenu, text="Track Expense", command=goToExpenseWindow)
expenseButton.pack()

aboutButton = tk.Button(mainMenu, text="About", command=showAbout)
aboutButton.pack()

exitButton = tk.Button(mainMenu, text="Exit", command=mainMenu.quit)
exitButton.pack()

# Create a tkinter instance for the expense window
expenseWindow = tk.Tk()
expenseWindow.title('PennyPilot: Track Expense')
expenseWindow.withdraw()  # Hide this window for now

# Create expense window widgets
welcomeLabel = tk.Label(expenseWindow, text="Welcome to PennyPilot Expense Tracker!")
welcomeLabel.pack()  # Positions the label in the window

# Create date entry field
dateLabel = tk.Label(expenseWindow, text="Date:")
dateLabel.pack()
dateEntry = tk.Entry(expenseWindow)
dateEntry.pack()

# Create amount entry field
amountLabel = tk.Label(expenseWindow, text="Amount:")
amountLabel.pack()
amountEntry = tk.Entry(expenseWindow)
amountEntry.pack()

# Create category entry field
categoryLabel = tk.Label(expenseWindow, text="Category:")
categoryLabel.pack()
categoryEntry = tk.Entry(expenseWindow)
categoryEntry.pack()

# Create description entry field
descriptionLabel = tk.Label(expenseWindow, text="Description:")
descriptionLabel.pack()
descriptionEntry = tk.Entry(expenseWindow)
descriptionEntry.pack()

# Create a button, link it to 'startTracking' function
startButton = tk.Button(expenseWindow, text="Start Tracking", command=startTracking)
startButton.pack()  # Positions the button in the window

# Create a back button, link it to 'goToMainMenuFromExpenseWindow' function
backButton = tk.Button(expenseWindow, text="Back to Main Menu", command=goToMainMenuFromExpenseWindow)
backButton.pack()

# Create a tkinter instance for the view expenses window
viewExpensesWindow = tk.Tk()
viewExpensesWindow.title('PennyPilot: View Expenses')
viewExpensesWindow.withdraw()  # Hide this window for now

# Create view expenses window widgets
expensesLabel = tk.Label(viewExpensesWindow, text="Your expenses:")
expensesLabel.pack()
expensesText = tk.Text(viewExpensesWindow)
expensesText.pack()
loadButton = tk.Button(viewExpensesWindow, text="Load Expenses", command=goToViewExpensesWindow)
loadButton.pack()
backButton = tk.Button(viewExpensesWindow, text="Back to Main Menu", command=goToMainMenuFromViewExpensesWindow)
backButton.pack()

# Start the Tkinter event loop
mainMenu.mainloop()
