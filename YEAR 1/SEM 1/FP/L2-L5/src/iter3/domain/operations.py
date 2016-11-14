'''
Created on 27 oct. 2016

@author: Tamas
'''
from iter3.domain.entities import get_apartment, get_type, create_expense, \
    get_amount

def expense_exists(transactions, apartment, expense_type):
    """Check if a given expense exists in the list of expenses.
    Args:
        apartment(uint): the apartment number to search for.
        expense_type(str): the type of the expense to search for.
    Returns:
        True if the expense exists,False otherwise.
    """
    
    # check if any transaction matches the input data
    for expense in transactions:
        if get_apartment(expense) == apartment and get_type(expense) == expense_type:
            return True
        
    return False

def apartment_exists(transactions, apartment):
    """Check if a given apartment number exists in the list of expenses.
    
    Args:
        transactions(list): the list containing the expenses.
        apartment(uint): the apartment number to search for.
    Returns:
        True if the apartment number exists,False otherwise.
        
    """
    # check if any apartment number matches the input data
    for expense in transactions:
        if get_apartment(expense) == apartment:
            return True
        
    return False

def expense_type_exists(transactions, expense_type):
    """Check if a given expense type exists in the list of expenses.
    
    Args:
        transactions(list): the list containing the expenses.
        expense_type(str): the expense type to search for.
    Returns:
        True if the expense type exists,False otherwise.
        
    """
    # check if any expense type matches the input data
    for expense in transactions:
        if get_type(expense) == expense_type:
            return True
        
    return False

def is_valid_expense_type(expense_type):
    """Check if a given expense type is valid.
    
    Args:
        expense_type(str): the type of the expense to check.
    Returns:
        True if the given expense type is valid,False otherwise.
        
    """
    expense_types = ("water", "heating", "electricity", "gas", "other")
    
    if expense_type not in expense_types:
        return False
    
    return True

def add_expense(transactions, apartment, expense_type, amount):
    """Add a new expense at the end of the transactions list.
    
    Args:
        apartment(uint): the apartment number.
        expense_type(str): the type of the expense.
        amount(uint): the amount of money.
    Returns:
        the transactions list containing the new expense.
    
    """
    transactions.append(create_expense(apartment, expense_type, amount))
    
    return transactions

def remove_expenses_by_apartment(transactions, apartment):
    """Remove expenses that have a certain apartment number.
    
    Args:
        transactions(list): the list containing the expenses.
        apartment(int): the apartment number of the expenses to be removed.
    Returns:
        the transactions list without the expenses having the given apartment number.
    
    """
    transactions[:] = [e for e in transactions if get_apartment(e) != apartment ]
    return transactions

def remove_expenses_by_type(transactions, expense_type):
    """Remove expenses that have a given type.
    
    Args:
        transactions(list): the list containing the expenses.
        expense_type(str): the type of the expenses to be removed.
    Returns:
        the transactions list without the expenses having the given type.
        
    """
    transactions[:] = [e for e in transactions if get_type(e) != expense_type]
    return transactions

def remove_expenses(transactions, apartment_start, apartment_end):
    """Remove all expenses from apartments between the numbers 'apartment_start' and 'apartment_end'.
    
    Args:
        transactions(list) - the list containing the expenses.
        apartment_start(uint) - first apartment.
        apartment_end(uint) - last apartment.
    Returns:
        the transactions list without the expenses that have the apartment number between 'apartment_start' and 'apartment_end'.
    
    """
    transactions[:] = [e for e in transactions if get_apartment(e) <= apartment_start or get_apartment(e) >= apartment_end]
    return transactions

def replace_expenses_amount(transactions, apartment, expense_type, amount):
    """Replace the amount of the expense having the given apartment number and type with a given amount value.
    
    Args:
        transactions(list): the list containing the expenses.
        apartment(uint) - the apartment number.
        expense_type(str) - the type of the expense.
        amount(uint) - the amount of money to be changed into.
    Returns:
        the new transactions list where the amount of an expense has been replaced with the given value.
        
    """     
    for expense in transactions:
        if get_type(expense) == expense_type and get_apartment(expense) == apartment:
            expense["amount"] = amount

    return transactions

def list_expenses(transactions):
    """Return the expenses."""
    return transactions

def list_expenses_by_apartment(transactions, apartment):
    """Return the expenses that have the apartment number 'apartment'."""
    return [expense for expense in transactions if get_apartment(expense) == apartment]
      
def list_expenses_greater(transactions, amount):
    """Return the expenses that have the amount smaller than a given value."""
    return [expense for expense in transactions if get_amount(expense) > amount]

def list_expenses_smaller(transactions, amount):
    """Return the expenses that have the amount greater than a given value."""
    return [expense for expense in transactions if get_amount(expense) < amount]
    
def list_expenses_equal(transactions, amount):
    """Return the expenses that have the amount equal to a given value"""
    return [expense for expense in transactions if get_amount(expense) == amount]

def sum_expenses_by_type(transactions, expense_type):
    """Return the sum of the expenses for a given expense_type."""
    return sum([get_amount(e) for e in transactions if get_type(e) == expense_type])

def max_expense_amount(transactions, apartment):
    """Get the maximum amount per each expense type for a given apartment number.
    
    Args:
        apartment(uint): the apartment number.
    Returns:
        the list of maximum expense amount having a given apartment number, for each type.
        
    """
    # the list of the expenses having the given apartment number
    expenses = [ e for e in transactions if get_apartment(e) == apartment]
    
    # the set of unique types in the list
    types = set([get_type(t) for t in expenses])
    
    # maximum expense value for each expense type
    max_values = [ max(expenses, key=lambda x: get_amount(x) if get_type(x) == t else 0) for t in types]
    
    return sorted(max_values,key = lambda x : get_amount(x))

def sort_expenses_by_apartment(transactions):
    """Create the list of apartments sorted ascending by total amount of expenses."""
    counter = {}
    
    for expense in transactions:
        counter[get_apartment(expense) ] = counter.get(get_apartment(expense), 0) + 1
        
    return sorted(counter.items(), key=lambda x:x[1])
        
def sort_expenses_by_type(transactions):
    """Create the list containing the total amount of expenses for each type,sorted ascending by amount of money."""
    counter = {}
    
    for expense in transactions:
        counter[get_type(expense)] = counter.get(get_type(expense), 0) + get_amount(expense)
        
    return sorted(counter.items(), key=lambda x: x[1])

def filter_expenses_by_type(transactions, expense_type):
    """Keep only the expenses having the given type."""
    transactions[:] = [e for e in transactions if get_type(e) == expense_type]
    return transactions
  
def filter_expenses_by_value(transactions, value):
    """Keep only the expenses having an amount of money smaller than the given value."""
    transactions[:] = [e for e in transactions if get_amount(e) < value]
    return transactions

def undo_command(transactions,backup):
    """ Undo the changes done to the transactions list."""
    transactions[:]=backup.pop()
    return transactions