'''
Created on 27 oct. 2016

@author: Tamas
'''

def get_apartment(expense):
    """Return the apartment number of the expense."""
    return expense["apartment"]

def get_type(expense):
    """Return the type of the expense."""
    return expense["type"]

def get_amount(expense):
    """Return the amount of money from the expense."""
    return expense["amount"]

def create_expense(apartment, expense_type, amount):
    """Create a new named dictionary to hold the expense data.
    
    Args:
        apartment(uint): the apartment number.
        expense_type(str): the type of the expense.
        amount(uint): the amount of money.
    Returns:
        the named dictionary containing the expense data.
    
    """
    return {"apartment":apartment, "type":expense_type, "amount":amount}