'''
Created on 14 nov. 2016

@author: Florin
'''
from domain.operations import add_student, modify_student_grade,\
    reduce_grades_group, get_students_by_hometown, get_students_by_code
from util.common import get_type

def ui_is_valid_code(code):
    if len(code)!=8:
        return False
    
    for i in range(0,4):
        if code[i].isdigit():
            return False
    
    for i in range(4,len(code)):
        if not code[i].isdigit():
            return False
        
    return True
        
def ui_add_student(students):
    code = input("code:")
    
    if not ui_is_valid_code(code):
        raise ValueError("Invalid student code provided.")
    
    if len(get_students_by_code(students,code))>0:
        raise ValueError("Duplicate student code.")
    
    name = input("name:")
    
    if len(name)<3:
        raise ValueError("Student name must be of length greater or equal to 3.")
    
    hometown = input("hometown:")
    
    if len(hometown)<3:
        raise ValueError("Student hometown must be of length greater or equal to 3.")
    
    grade = input("grade:")
    
    if get_type(grade) is not int:
        raise ValueError("The student grade must be an integer.")
    
    grade = int(grade)
    
    if grade < 1 or grade > 10:
        raise ValueError("Invalid grade value provided.")
    
    add_student(students,code,name,hometown,grade)

def ui_modify_grade(students):
    code = input("code:")
    
    if not ui_is_valid_code(code):
        raise ValueError("Invalid student code provided.")
    
    new_grade = input("new grade:")
    
    if get_type(new_grade) is not int:
        raise ValueError("The student grade must be an integer.")
    
    new_grade=int(new_grade)
    
    if new_grade<1 or new_grade > 10:
        raise ValueError("Invalid grade provided.")
    
    if len(get_students_by_code(students, code))==0:
        raise ValueError("No student with the given code exists.")
    
    modify_student_grade(students,code,new_grade)


def ui_penalize_group(students):
    group = input("group:")
    
    if len(group)!=2:
        raise ValueError("The length of the students group must be equal to 2.")
    
    reduce_grades_group(students,group,10)

def ui_list_by_hometown(students):
    hometown = input("hometown:")
        
    if len(hometown)<3:
        raise ValueError("Hometown length must be greater or equal to 3.")
    
    for student in get_students_by_hometown(students, hometown):
        print(student)
    
def ui_list_all(students):
    for student in students:
        print(student)

def ui_print_menu(args=None):
    print("0.List all.") # only for testing purposes
    print("1.Add a student.")
    print("2.Modify the grade of a student.")
    print("3.Penalize students of a given group.")
    print("4.Show all students with a given hometown sorted decreasing by their grade.")
    print("5.Exit")
    
def ui_read_command():
    command = input("command:")
    
    if get_type(command) is not int:
        raise ValueError("Invalid command value provided.")
    
    return int(command)

def load_predefined_data(students):
    add_student(students, "miie1234", "Ion1", "Cluj", 9)
    add_student(students, "miie1235", "Ion2", "Satu Mare", 8)
    add_student(students, "miie1236", "Ion3", "Alba Iulia", 7)
    add_student(students, "miie1237", "Ion4", "Alba Iulia", 6)
    add_student(students, "miie1838", "Ion5", "Alba Iulia", 5)
    add_student(students, "miie1739", "Ion6", "Alba Iulia", 4)
    add_student(students, "miie1630", "Ion7", "Alba Iulia", 3)
    add_student(students, "miie1531", "Ion8", "Alba Iulia", 2)
    add_student(students, "miie1432", "Ion9", "Alba Iulia", 3)
    add_student(students, "miie1333", "Ion0", "Baia Mare", 10)
    
def run_app():
    students = []
    
    ui_print_menu()
    
    load_predefined_data(students)
    
    commands = {0:ui_list_all,1:ui_add_student,2:ui_modify_grade,3:ui_penalize_group,4:ui_list_by_hometown}
    
    while True:
        command = ui_read_command()
        
        # exit
        if command==len(commands)+1:
            break
        
        if command<0 or command>len(commands):
            print("Invalid command index provided.")
        try:
            commands[command](students)
        except ValueError as ve:
            print(ve)
            