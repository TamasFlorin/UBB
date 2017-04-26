'''
Created on 14 nov. 2016

@author: Florin
'''

def create_student(code,name,hometown,grade):
    """Create a new dictionary to hold the student information.
    Args:
        code(str): the code of the student
        name(str): the name of the student
        hometown(str): the hometown of the student
        grade(int): the grade of the student
    Returns:
        a new dictionary containing the student data.
    """
    return {"code":code,"name":name,"hometown":hometown,"grade":grade}

def get_student_code(student):
    """Get the student code from the dictionary"""
    return student["code"]

def get_student_name(student):
    """Get the student name for the dictionary."""
    return student["name"]

def get_student_hometown(student):
    """Get the student hometown from the dictionary."""
    return student["hometown"]

def get_student_grade(student):
    """Get the student grade from the dictionary."""
    return student["grade"]
