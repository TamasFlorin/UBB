'''
Created on 14 nov. 2016

@author: Florin
'''
from test_entities import test_create_student
from test_operations import test_add_student, test_modify_student_grade,\
    test_penalize_students_group, test_get_students_by_hometown

def test_all():
    test_create_student()
    test_add_student()
    test_modify_student_grade()
    test_penalize_students_group()
    test_get_students_by_hometown()

if __name__ == '__main__':
    test_all()