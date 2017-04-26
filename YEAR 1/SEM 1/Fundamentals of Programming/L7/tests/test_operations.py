'''
Created on 14 nov. 2016

@author: Florin
'''
from domain.operations import add_student,modify_student_grade,\
    reduce_grades_group, get_students_by_hometown

def test_add_student():
    students = []
    add_student(students,"miie1234","John","Alba Iulia",10)
    
    assert len(students)==1
    
    add_student(students,"miie1246","Ion","Cluj",9)
    
    assert len(students)==2
    
def test_modify_student_grade():
    students = []
    
    add_student(students,"miie1234","John","Alba Iulia",10)
    
    modify_student_grade(students,"miie1234",9)
    
    assert students[0]["grade"]==9
    
def test_penalize_students_group():
    students = []
    
    add_student(students,"miie1234","John","Alba Iulia",10)
    add_student(students,"miie1246","Ion","Cluj",9)
    
    reduce_grades_group(students,"12",10)
    
    assert students[0]["grade"]==9 and students[1]["grade"]==8
    
def test_get_students_by_hometown():
    students = []
    add_student(students,"miie1234","John","Alba Iulia",10)
    add_student(students,"miie1246","Ion","Cluj",9)
    add_student(students,"miie1230","Razvan","Cluj",10)
    add_student(students,"miie1241","Vlad","Cluj",9)
    
    res = get_students_by_hometown(students,"Cluj")
    
    assert len(res)==3