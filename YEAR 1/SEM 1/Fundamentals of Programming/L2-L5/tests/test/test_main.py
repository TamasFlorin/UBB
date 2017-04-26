'''
Created on 27 oct. 2016

@author: Tamas
'''
from test.domain.test_entities import test_all_entities
from test.domain.test_operations import test_all_operations
from test.util.test_pattern import test_argument_functions
from iter3.ui.initializer import run_app

def main():
    test_all_entities()
    test_all_operations()
    test_argument_functions()
    run_app()

if __name__ == '__main__':
    main()