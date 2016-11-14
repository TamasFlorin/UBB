'''
Created on 14 nov. 2016

@author: Florin
'''
from domain.entities import create_student, get_student_code,\
    get_student_hometown, get_student_grade

def add_student(students,code,name,hometown,grade):
    """Add a new student to the list of students.
    Args:
        code(str): the code of the student
        name(str): the name of the student
        hometown(str): the hometown of the student
        grade(uint): the grade of the student
    Returns:
        the list of students containing the new student entry.
    """
    students.append(create_student(code,name,hometown,grade))
    return students

def modify_student_grade(students,code,new_grade):
    """Modify a student's grade by a given student code.
    Args:
        students(list): the list of students
        code(str): the code of the student for which the grade will be changed
        new_grade(uint): the new grade of the student
    Returns:
        the list of students with the modified data.
    """
    list(filter(lambda x: (get_student_code(x)==code),students))[0]["grade"] = new_grade
    
    return students
            
def reduce_grades_group(students,group,percent):
    """Reduce the grade for an entire students group by a given percent.
    Args:
        students(list): the list of students
        group(str): the group for which to reduce the grade
        percent(int): the percent with which to reduce the grade
    Returns:
        the list of students after the changes.
    """     
    for student in students:
        if get_student_code(student)[4:6]==group:
            student["grade"]=student["grade"]*(100-percent)//100
            
    return students

def get_students_by_hometown(students,hometown):
    """Get a list of students that have a given hometown.
    Args:
        students(list): the list of students
        hometown(str): the hometown of the student
    Returns:
        the list of students having the given hometown.
    """
    return sorted(list(filter(lambda x:get_student_hometown(x)==hometown,students)),key = lambda x: get_student_grade(x),reverse=True)

def get_students_by_code(students,code):
    """Get a student by it's code.
    Args:
        students(list): the list of the students
        code(str): the code of the student to search for
    Returns:
        the student matching the given code.
    """
    return list(filter(lambda x: get_student_code(x)==code,students))
        