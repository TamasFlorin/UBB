'''
Created on 29 oct. 2016

@author: Tamas
'''
from iter3.domain.entities import get_apartment, get_type, get_amount
from iter3.domain.operations import is_valid_expense_type, add_expense, \
    apartment_exists, remove_expenses_by_apartment, expense_type_exists, \
    remove_expenses_by_type, remove_expenses, expense_exists, \
    replace_expenses_amount, list_expenses, list_expenses_by_apartment, \
    list_expenses_greater, list_expenses_smaller, list_expenses_equal, \
    sum_expenses_by_type, max_expense_amount, sort_expenses_by_apartment, \
    sort_expenses_by_type, filter_expenses_by_type, filter_expenses_by_value, \
    undo_command

def ui_add_expense(transactions,backup, apartment, expense_type, amount):
    """Add an expense to the end of the transactions list.
    
    Args:
        transactions(list): the list containing the expenses.
        apartment(uint): the apartment number.
        expense_type(str): the type of the expense.
        amount(uint): the amount of money.
    Returns:
        None
    Raises:
        ValueError: if the apartment number is negative
                    if the amount of money is negative
                    if the expense type is invalid
                    
    """
    apartment = int(apartment)
    amount = int(amount)
    
    if apartment < 0:
        raise ValueError("Negative value given for apartment number.")
    
    if amount < 0:
        raise ValueError("Negative value given for the amount.")
    
    if not is_valid_expense_type(expense_type.lower()):
        raise ValueError("Invalid expense type provided.")
    
    # if expense_exists(transactions, apartment, expense_type):
        # raise ValueError("Transaction already in list.")
    
    # backup the data before making any changes
    backup.append(transactions[:])
    
    add_expense(transactions, apartment, expense_type.lower(), amount)

def ui_remove_expenses_by_apartment(transactions,backup, apartment):
    """Remove the expenses that have the apartment number equal to a given value.
    Args:
        transactions(list) - the list containing the expenses.
        apartment(uint) - the apartment number.
    Returns:
        None
    Raises:
        ValueError: if the list is empty.
                    if the apartment number is not an unsigned integer.
                    if the apartment does not exist in the list.
                    
    """
    if len(transactions) == 0:
        raise ValueError("Cannot remove values from empty list.")
    
    apartment = int(apartment)
    
    if apartment < 0:
        raise ValueError("Negative value given for the apartment number.")
    
    if not apartment_exists(transactions, apartment):
        raise ValueError("No expense with apartment number %d exists." % apartment)
    
    # backup the data before making any changes
    backup.append(transactions[:])
    
    remove_expenses_by_apartment(transactions, apartment)

def ui_remove_expenses_by_type(transactions,backup, expense_type):
    """Remove expenses that have a given type.
    
    Args:
        transactions(list): the list containing the expenses.
        expense_type(str): the expense type.
    Raises:
        ValueError: if the list is empty.
                    if the expense_type is invalid.
                    if the expense_type does not exist in the list.
                    
    """
    if len(transactions) == 0:
        raise ValueError("Cannot remove values from empty list.")
    
    expense_type = expense_type.lower()
    if not is_valid_expense_type(expense_type):
        raise ValueError("Invalid expense type provided.")
    
    if not expense_type_exists(transactions, expense_type):
        return ValueError("No expense with type %s exists." % expense_type)
    
    # backup the data before making any changes
    backup.append(transactions[:])
    
    remove_expenses_by_type(transactions, expense_type)
    
def ui_remove_expenses(transactions,backup, apartment_start, apartment_end):
    """Remove expenses that have the apartment number inside the bounds (apartment_start,apartment_end).
    
    Args:
        transactions(list): the list containing the expenses.
        apartment_start(uint): first apartment number.
        apartment_end(uint): last apartment number.
    Raises:
        ValueError: if the transactions list is empty.
                    if apartment_start or apartment_end are not valid unsigned integers.
                    
    """
    if len(transactions) == 0:
        raise ValueError("Cannot remove values from empty list.")
    
    apartment_start = int(apartment_start)
    apartment_end = int(apartment_end)
    
    if apartment_start < 0 or apartment_end < 0:
        raise ValueError("Negative value given for the apartment number.")
    
    # backup the data before making any changes
    backup.append(transactions[:])
    
    remove_expenses(transactions, apartment_start, apartment_end)
    
def ui_replace_expenses_amount(transactions,backup, apartment, expense_type, amount):
    """Replace the amount of the expenses with the given type for the given apartment number with the given amount.
    
    Args:
        transactions(list): the list containing the expenses.
        apartment(uint): the apartment number.
        expense_type(str): the type of the expense.
        amount(uint): the amount of money to be changed into.
    Returns:
        None
    Raises:
        ValueError: if the list is empty.
                    if the apartment number or amount are invalid unsigned integers.
                    if the expense_type is invalid.
                    if no expense with the provided data exists.
                    
    """
    if len(transactions) == 0:
        raise ValueError("Cannot replace values in empty list.")
    
    apartment = int(apartment)
    
    if apartment < 0:
        raise ValueError("Negative value given for the apartment number.")
    
    expense_type = expense_type.lower()
    if not is_valid_expense_type(expense_type):
        raise ValueError("Invalid expense type provided.")
    
    amount = int(amount)
    
    if amount < 0:
        raise ValueError("Negative value given for the amount.")
    
    if not expense_exists(transactions, apartment, expense_type):
        raise ValueError("No expenses with provided data could be found.")
    # backup the data before making any changes
    backup.append(transactions[:])
    
    replace_expenses_amount(transactions, apartment, expense_type, amount)
    
def ui_pretty_print(transactions):
    """Print the list in 'prettier' format."""
    for expense in transactions:
        print("Apartment = %d with type = %s and an amount of money = %d" % (get_apartment(expense), get_type(expense), get_amount(expense)))
            
def ui_list_expenses(transactions,backup):
    """Write the expenses from the transactions list.
    
    Args:
        transactions(list): the list containing the expenses.
    Returns:
        None
    Raises:
        ValueError: if the transactions list is empty.
        
    """
    if len(transactions) == 0:
        raise ValueError("The list is empty.")
    
    ui_pretty_print(list_expenses(transactions))
            
def ui_list_expenses_by_apartment(transactions,backup, apartment):
    """Write the expenses that have a given apartment number.
    
    Args:
        transactions(list): the list containing the expenses.
        apartment(uint): the apartment number.
    Returns:
        None
    Raises:
        ValueError: if the transactions list is empty.
                    if the apartment number is an invalid unsigned integer.
        
    """
    if len(transactions) == 0:
        raise ValueError("The list is empty.")
    
    apartment = int(apartment)
    
    if apartment < 0:
        raise ValueError("Negative value given for the apartment number.")
    
    if not apartment_exists(transactions, apartment):
        raise ValueError("No expense with apartment number %d could be found." % apartment)
    
    ui_pretty_print(list_expenses_by_apartment(transactions, apartment))
    
def ui_list_expenses_greater(transactions,backup, amount):
    """Write the expenses that have the amount of money greater than a given value.
    
    Args:
        transactions(list): the list containing the expenses.
        amount(uint): the amount of money.
    Returns:
        None
    Raises:
        ValueError: if the transactions list is empty.
                    if the amount is an invalid unsigned integer.
                    if no amount greater than the given value exists.
                    
    """
    if len(transactions) == 0:
        raise ValueError("The list is empty.")
    
    amount = int(amount)
    
    if amount < 0:
        raise ValueError("Negative value given for the amount.")
    
    expenses = list_expenses_greater(transactions, amount)
    
    if len(expenses) == 0:
        raise ValueError("No amount value greater than %d exists." % amount)
    
    ui_pretty_print(list_expenses_greater(transactions, amount))
    
def ui_list_expenses_smaller(transactions,backup, amount):
    """Write the expenses that have the amount of money smaller than a given value.
    
    Args:
        transactions(list): the list containing the expenses.
        amount(uint): the amount of money.
    Returns:
        None
    Raises:
        ValueError: if the transactions list is empty
                    if the amount is an invalid unsigned integer.
                    if no amount smaller than the given value exists.
    
    """
    if len(transactions) == 0:
        raise ValueError("The list is empty.")
    
    amount = int(amount)
    
    if amount < 0:
        raise ValueError("Negative value given for the amount.")
    
    expenses = list_expenses_smaller(transactions, amount)
    
    if len(expenses) == 0:
        raise ValueError("No amount value smaller than %d exists." % amount)
    
    ui_pretty_print(list_expenses_smaller(transactions, amount))

def ui_list_expenses_equal(transactions,backup, amount):
    """Write the expenses that have the amount of money equal to a given value.
    Args:
        transactions(list): the list containing the expenses.
        amount(uint): the amount of money.
    Returns:
        None
    Raises:
        ValueError: if the transactions list is empty.
                    if the amount is an invalid unsigned integer.
                    if no amount equal to the given value exists.
    """
    
    if len(transactions) == 0:
        raise ValueError("The list is empty.")
    
    amount = int(amount)
    
    if amount < 0:
        raise ValueError("Negative value given for the the amount.")
    
    expenses = list_expenses_equal(transactions, amount)
    
    if len(expenses) == 0:
        raise ValueError("No amount equal to %d exists." % amount)
    
    ui_pretty_print(list_expenses_equal(transactions, amount)) 

def ui_sum_expenses_by_type(transactions,backup, expense_type):
    """Write the sum of the amount of money for each expense type.
    
    Args:
        transactions(list): the list containing the expenses.
        expense_type: the type of the expense.
    Returns:
        None
    Raises:
        ValueError: if the transactions list is empty.
                    if the expense type is invalid.
                    if the expense type does not exist in the list.
                    
    """
    if len(transactions) == 0:
        raise ValueError("The list is empty.")
    
    if not is_valid_expense_type(expense_type):
        raise ValueError("Invalid expense type provided.")
    
    expense_type = expense_type.lower()
    
    if not expense_type_exists(transactions, expense_type):
        raise ValueError("No expense with type %s exists." % expense_type)
    
    print("The sum for type '%s' is %d." % (expense_type, sum_expenses_by_type(transactions, expense_type)))
    
def ui_max_expense_amount(transactions,backup, apartment):
    """Write the maximum amount of money per each expense type for a given apartment number.
    
    Args:
        transactions(list): the list containing the expenses.
        apartment(uint): the apartment number.
    Returns:
        None
    Raises:
        ValueError: if the transactions list is empty.
                    if the apartment number is an invalid unsigned integer.
                    if the apartment number does not exist in the list.
                    
    """
    if len(transactions) == 0:
        raise ValueError("The transactions list is empty.")
    
    apartment = int(apartment)
    
    if apartment < 0:
        raise ValueError("Negative value given for the apartment number.")
    
    if not apartment_exists(transactions, apartment):
        raise ValueError("No expense with apartment number %d could be found." % apartment)
    
    ui_pretty_print([m for m in max_expense_amount(transactions, apartment)])
        
def ui_sort_expenses_by_apartment(transactions,backup):
    """Write the list of apartments sorted ascending by total amount of expenses.
    Args:
        transactions(list): the list containing the expenses.
    Returns:
        None
    Raises:
        ValueError: if the list is empty
    """
    
    if len(transactions) == 0:
        raise ValueError("The transactions list is empty.")
    
    print("====Sorted by apartment====")
    for apartment in sort_expenses_by_apartment(transactions):
        print("apartment=%d with count=%d" % (apartment))
    print("===========================")
    
def ui_sort_expenses_by_type(transactions,backup):
    """Write the total amount of expenses for each type,sorted ascending by amount of money.
    Args:
        transactions(list): the list containing the expenses.
    Returns:
        None
    Raises:
        ValueError: if the transactions list is empty.
    """
    
    if len(transactions) == 0:
        raise ValueError("The transactions list is empty.")    
    
    print("====Sorted by type====")
    for expense_type in sort_expenses_by_type(transactions):
        print("expense type = %s with total amount = %d" % (expense_type))
    print("======================")
    
def ui_filter_expenses_by_type(transactions,backup, expense_type):
    """Keep only the expenses that have a given type.
    
    Args:
        transactions(list): the list containing the xpenses.
        expense_type: the type of the expense.
    Returns:
        None
    Raises:
        ValueError: if the transactions list is empty.
                    if the expense type is invalid.
                    if the expense type does not exist in the transactions list.
                    
    """
    if len(transactions) == 0:
        raise ValueError("The transactions list is empty.")
    
    if not is_valid_expense_type(expense_type):
        raise ValueError("Invalid expense type provided.")
    
    expense_type = expense_type.lower()
    if not expense_type_exists(transactions, expense_type):
        raise ValueError("No expense with type %s could be found." % expense_type)
    
    # backup the data before making any changes
    backup.append(transactions[:])
    
    filter_expenses_by_type(transactions, expense_type)
    
def ui_filter_expenses_by_value(transactions,backup, value):
    """ Keep only the expenses having an amount of money smaller than a given value.
    Args:
        transactions(list): the list containing the expenses.
        amount(uint): the amount of money
    Returns:
        None
    Raises:
        ValueError: if the transactions list is empty.
                    if the amount is an invalid unsigned integer.
    """
    
    if len(transactions) == 0:
        raise ValueError("List is empty.")
    
    value = int(value)
    
    if value < 0:
        raise ValueError("Negative value given for the amount.")
    
    # backup the data before making any changes
    backup.append(transactions[:])
    
    filter_expenses_by_value(transactions, value)

def ui_undo_command(transactions,backup):
    
    if len(backup)==0:
        raise ValueError("Nothing to undo.")
    
    undo_command(transactions, backup)
    
def ui_help(args=None,backup=None):
    """Write the commands and their usage."""
    print("Available commands:")
    commands = register_commands()
    count = 0
    for key,command in sorted(commands.items()):
        for c in command:
            print("%d. %s %s" %(count,key,get_arg_names(c)))
            count +=1
        
def create_command(function, pattern="",arg_names=""):
    """Return a new named dictionary containing the function and it's pattern."""
    return {"function":function, "pattern":pattern,"arg_names":arg_names}

def get_pattern(command):
    """Return the pattern of a command."""
    return command["pattern"]

def get_function(command):
    """Return the function of a command."""
    return command["function"]

def get_arg_names(command):
    return command["arg_names"]

def register_commands():
    return {
        "add" :  (create_command(ui_add_expense, "int string int","<apartment> <type> <amount>"),),
        "remove":(
                   create_command(ui_remove_expenses_by_apartment, "int","<apartment>"),
                   create_command(ui_remove_expenses_by_type, "string","<type>") ,
                   create_command(ui_remove_expenses, "int to int","<start apartment> to <end apartment>")
                 ),
        "replace":(create_command(ui_replace_expenses_amount, "int string with int","<apartment> <type> with <amount>"),),
        "list" :  (create_command(ui_list_expenses),
                   create_command(ui_list_expenses_by_apartment, "int","<apartment>"),
                   create_command(ui_list_expenses_greater, "> int","> <amount>"),
                   create_command(ui_list_expenses_smaller, "< int","< <amount>"),
                   create_command(ui_list_expenses_equal, "= int","= <amount>")),
        "sum":(create_command(ui_sum_expenses_by_type, "string","<type>"),),
        "max":(create_command(ui_max_expense_amount, "int","<apartment>"),),
        "sort":(create_command(ui_sort_expenses_by_apartment,"apartment", arg_names="apartment"),
                create_command(ui_sort_expenses_by_type,"type",arg_names= "type")),
        "filter":(
                   create_command(ui_filter_expenses_by_type, "string","<type>"),
                   create_command(ui_filter_expenses_by_value, "int","<value>"),),
        "help":(create_command(ui_help),),
        "undo":(create_command(ui_undo_command),),
        "quit":(create_command(None),)
    }

def load_predefined_data(transactions):
    add_expense(transactions, 1, "gas", 100)
    add_expense(transactions, 1, "other", 50)
    add_expense(transactions, 2, "water", 20)
    add_expense(transactions, 3, "electricity", 70)
    add_expense(transactions, 3, "heating", 100)
    add_expense(transactions, 5, "gas", 200)
    add_expense(transactions, 6, "other", 500)
    add_expense(transactions, 7, "heating", 1000)
    add_expense(transactions, 7, "other", 300)
    add_expense(transactions, 8, "gas", 900)
    add_expense(transactions, 9, "electricity", 250)