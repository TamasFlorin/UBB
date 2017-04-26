'''
Created on 27 oct. 2016

@author: Tamas
'''
from iter3.domain.operations import add_expense, remove_expenses_by_apartment, \
    remove_expenses_by_type, remove_expenses, replace_expenses_amount, \
    list_expenses, list_expenses_by_apartment, list_expenses_greater, \
    list_expenses_smaller, list_expenses_equal, sum_expenses_by_type,\
    max_expense_amount, sort_expenses_by_apartment, sort_expenses_by_type,\
    filter_expenses_by_type, filter_expenses_by_value, undo_command


def test_add_expense():
    transactions = []
    
    add_expense(transactions,12,"gas",100)
    assert len(transactions)==1
    
    add_expense(transactions,1,"heating",200)
    assert len(transactions)==2
    
def test_remove_expense_by_apartment():
    transactions = []
    
    add_expense(transactions, 1, "gas", 100)
    add_expense(transactions, 1, "heating", 50)
    
    remove_expenses_by_apartment(transactions,1)
    assert len(transactions)==0
    
def test_remove_expense_by_type():
    transactions = []
    
    add_expense(transactions, 1, "gas", 20)
    add_expense(transactions, 2, "gas", 50)
    add_expense(transactions, 3, "heating", 20)
    
    remove_expenses_by_type(transactions,"gas")
    assert len(transactions)==1
    
def test_remove_expenses():
    transactions = []
    
    add_expense(transactions, 1, "gas", 20)
    add_expense(transactions, 2, "gas", 50)
    add_expense(transactions, 3, "heating", 20)
    
    remove_expenses(transactions,1,3)
    
    assert len(transactions)==2
    
def test_replace_expense_ammount():
    transactions = []
    
    add_expense(transactions,1,"heating",100)
    
    replace_expenses_amount(transactions,1,"heating",200)
    
    assert transactions[0]["amount"]==200
    
def test_list_expenses():
    transactions = []
    
    add_expense(transactions, 1, "gas", 20)
    add_expense(transactions, 2, "gas", 50)
    add_expense(transactions, 3, "heating", 20)
    
    assert transactions == list_expenses(transactions)
    
def test_list_expenses_by_apartment():
    transactions = []
    
    add_expense(transactions, 1, "gas", 100)
    add_expense(transactions, 2, "gas", 50)
    add_expense(transactions, 3, "heating", 20)
    
    assert list_expenses_by_apartment(transactions,1)==[{'apartment':1, "type":"gas", "amount":100}]
    assert list_expenses_by_apartment(transactions,2)==[{'apartment':2, "type":"gas", "amount":50} ]
    
def test_list_expenses_greater():
    transactions = []
    
    add_expense(transactions, 1, "gas", 100)
    add_expense(transactions, 2, "gas", 50)
    add_expense(transactions, 3, "heating", 20)
    
    assert list_expenses_greater(transactions,50) == [{'apartment':1, "type":"gas", "amount":100}]
    
def test_list_expenses_smaller():
    transactions = []
    
    add_expense(transactions, 1, "gas", 100)
    add_expense(transactions, 2, "gas", 50)
    add_expense(transactions, 3, "heating", 20)
    
    assert list_expenses_smaller(transactions,100)==[ {'apartment':2, "type":"gas", "amount":50},{'apartment':3, "type":"heating", "amount":20}]
    
def test_list_expenses_equal():
    transactions = []
    
    add_expense(transactions, 1, "gas", 100)
    add_expense(transactions, 2, "electricity", 100)
    
    assert list_expenses_equal(transactions,100)==[ {'apartment':1, "type":"gas", "amount":100},{'apartment':2, "type":"electricity", "amount":100}]

def test_sum_expenses_by_type():
    transactions = []
    
    add_expense(transactions, 1, "gas", 100)
    add_expense(transactions, 2, "electricity", 200)
    add_expense(transactions, 3, "electricity", 50)
    
    assert sum_expenses_by_type(transactions,"electricity")==250
    
def test_max_expense_amount():
    transactions = []
    
    add_expense(transactions, 1, "gas", 100)
    add_expense(transactions, 1, "electricity", 200)
    add_expense(transactions, 1, "electricity", 50)
    add_expense(transactions, 1, "gas", 20)
    
    max_expenses = max_expense_amount(transactions,1)
    
    assert max_expenses[0]["amount"] == 100
    assert max_expenses[1]["amount"] == 200
    
def test_sort_expenses_by_apartment():
    transactions = []
    
    add_expense(transactions, 1, "gas", 100)
    add_expense(transactions, 1, "electricity", 200)
    add_expense(transactions, 2, "electricity", 50)
    add_expense(transactions, 2, "gas", 20)
    
    assert sort_expenses_by_apartment(transactions)==[(1, 2), (2, 2)]
    
def test_sort_expenses_by_type():
    transactions = []
    
    add_expense(transactions, 1, "gas", 100)
    add_expense(transactions, 1, "electricity", 200)
    add_expense(transactions, 2, "electricity", 50)
    add_expense(transactions, 2, "gas", 20)
    
    assert sort_expenses_by_type(transactions) == [('gas', 120), ('electricity', 250)]
    
def test_filter_expenses_by_type():
    transactions = []
    
    add_expense(transactions, 1, "gas", 100)
    add_expense(transactions, 1, "electricity", 200)
    add_expense(transactions, 2, "electricity", 50)
    add_expense(transactions, 2, "gas", 20)
    
    assert filter_expenses_by_type(transactions,"gas")==[{'type': 'gas', 'amount': 100, 'apartment': 1}, {'type': 'gas', 'amount': 20, 'apartment': 2}]

def test_filter_expenses_by_value():
    transactions = []
    
    add_expense(transactions, 1, "gas", 100)
    add_expense(transactions, 1, "electricity", 200)
    add_expense(transactions, 2, "electricity", 50)
    add_expense(transactions, 2, "gas", 20)
    
    assert filter_expenses_by_value(transactions,100) == [{'amount': 50, 'apartment': 2, 'type': 'electricity'}, {'amount': 20, 'apartment': 2, 'type': 'gas'}]

def test_undo_command():
    transactions = []
    backup = []
    
    add_expense(transactions, 1, "gas", 100)
    backup.append(transactions[:])
    
    undo_command(transactions,backup)
    
    assert len(transactions)==0
    
def test_all_operations():
    test_add_expense()
    test_remove_expense_by_apartment()
    test_remove_expense_by_type()
    test_remove_expenses()
    test_replace_expense_ammount()
    test_list_expenses()
    test_list_expenses_by_apartment()
    test_list_expenses_greater()
    test_list_expenses_smaller()
    test_list_expenses_equal()
    test_sum_expenses_by_type()
    test_max_expense_amount()
    test_sort_expenses_by_apartment()
    test_sort_expenses_by_type()
    test_filter_expenses_by_type()
    test_filter_expenses_by_value()