'''
Created on 29 oct. 2016

@author: Tamas
'''
from iter3.ui.base import load_predefined_data
from iter3.ui.console import run_console
from iter3.ui.menu import run_menu


def print_choises():
    print("1.Command based UI")
    print("2.Menu based UI")

def read_choice():
    while True:
        try:
            choice = input("choice: ")
            if choice in ("1","2"):
                return choice
        except:
            print("Invalid choice selected.")

def run_app():
    transactions = []
    
    # for testing purposes
    load_predefined_data(transactions)
    
    backup = []
    
    print_choises()
    
    if read_choice() == "1":
        run_console(transactions,backup)
    else:
        run_menu(transactions, backup)