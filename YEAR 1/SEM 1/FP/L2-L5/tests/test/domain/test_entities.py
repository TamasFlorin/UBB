'''
Created on 28 oct. 2016

@author: Tamas
'''
from iter3.domain.entities import create_expense, get_apartment, get_amount,\
    get_type

def test_create_expense(): 
    assert {"apartment":1,"type":"gas","amount":100}==create_expense(1, "gas", 100)
    assert {"apartment":2,"type":"electricity","amount":50}==create_expense(2, "electricity", 50)
    assert {"apartment":3,"type":"heating","amount":200}==create_expense(3, "heating", 200)
    
def test_get_apartment():
    assert get_apartment({"apartment":1, "type":"gas", "amount":100})==1
    assert get_apartment({"apartment":2, "type":"gas", "amount":100})==2
    assert get_apartment({"apartment":3, "type":"gas", "amount":100})==3
    
    
def test_get_amount():
    assert get_amount({"apartment":1, "type":"gas", "amount":200})==200
    assert get_amount({"apartment":1, "type":"gas", "amount":500})==500
    assert get_amount({"apartment":1, "type":"gas", "amount":100})==100
    
def test_get_type():
    assert get_type({"apartment":1, "type":"gas", "amount":50})=="gas"
    assert get_type({"apartment":1, "type":"heating", "amount":50})=="heating"
    assert get_type({"apartment":1, "type":"electricity", "amount":50})=="electricity"
    
def test_all_entities():
    test_create_expense()
    test_get_apartment()
    test_get_amount()
    test_get_type()
