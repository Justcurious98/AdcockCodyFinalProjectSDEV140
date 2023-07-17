"""
Author:  Cody Adcock
Date written: 07/0/23
Assignment:   Final Project
Short Desc:   An application to help navigate personal finances
"""

import tkinter as tk
from tkinter import messagebox

# Global variables
root = None
dateEntry = None
amountEntry = None
categoryEntry = None
descriptionEntry = None
welcomeLabel = None

# Function to be executed when the button is clicked
def startTracking():
    date = dateEntry.get()
    amount = amountEntry.get()
    category = categoryEntry.get()
    description = descriptionEntry.get()
    welcomeLabel.config(text=f"Tracking started for expense: {amount} on {date} for {category}, {description}") 

def goToExpenseWindow():
    # Hide the mainMenu window
    mainMenu.withdraw()
    
    # Access global variables
    global root, dateEntry, amountEntry, categoryEntry, descriptionEntry, welcomeLabel
    
    root = tk.Tk()
    root.title('PennyPilot: Navigating Your Finances')

    # Create a label
    welcomeLabel = tk.Label(root, text="Welcome to PennyPilot Expense Tracker!")
    welcomeLabel.pack()  # Positions the label in the window

    # Create date entry field
    dateLabel = tk.Label(root, text="Date:")
    dateLabel.pack()
    dateEntry = tk.Entry(root)
    dateEntry.pack()

    # Create amount entry field
    amountLabel = tk.Label(root, text="Amount:")
    amountLabel.pack()
    amountEntry = tk.Entry(root)
    amountEntry.pack()

    # Create category entry field
    categoryLabel = tk.Label(root, text="Category:")
    categoryLabel.pack()
    categoryEntry = tk.Entry(root)
    categoryEntry.pack()

    # Create description entry field
    descriptionLabel = tk.Label(root, text="Description:")
    descriptionLabel.pack()
    descriptionEntry = tk.Entry(root)
    descriptionEntry.pack()

    # Create a button, link it to 'startTracking' function
    startButton = tk.Button(root, text="Start Tracking", command=startTracking)
    startButton.pack()  # Positions the button in the window

    # Create a back button, link it to 'goToMainMenu' function
    backButton = tk.Button(root, text="Back to Main Menu", command=goToMainMenu)
    backButton.pack()

    root.mainloop()

def goToMainMenu():
    # Hide the expense tracking window
    root.withdraw()
    
    # Show the main menu again
    mainMenu.deiconify()

def showAbout():
    messagebox.showinfo("About PennyPilot", "PennyPilot is a personal finance tracking application. It helps you navigate your financial journey.")

# Create a tkinter instance for the main menu window
mainMenu = tk.Tk()  
mainMenu.title('PennyPilot: Main Menu')

# Create main menu buttons
expenseButton = tk.Button(mainMenu, text="Track Expense", command=goToExpenseWindow)
expenseButton.pack()

aboutButton = tk.Button(mainMenu, text="About", command=showAbout)
aboutButton.pack()

exitButton = tk.Button(mainMenu, text="Exit", command=mainMenu.quit)
exitButton.pack()

mainMenu.mainloop()
