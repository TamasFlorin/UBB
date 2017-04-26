'''
Created on 28 oct. 2016

@author: Tamas
'''
from iter3.util.pattern import argument_type, arguments_pattern

def test_argument_type():
    assert argument_type("string")==str
    assert argument_type("12")==int
    assert argument_type("1.2")==float
    assert argument_type("12a")==str

def test_arguments_pattern():
    assert arguments_pattern(["1","to","2"])=="int to int"
    assert arguments_pattern(["1","gas","1"])=="int string int"
    assert arguments_pattern(["1", "gas", "with", "100"])=="int string with int"
    
def test_argument_functions():
    test_argument_type()
    test_arguments_pattern()