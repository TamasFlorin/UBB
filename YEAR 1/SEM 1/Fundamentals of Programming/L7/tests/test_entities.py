'''
Created on 14 nov. 2016

@author: Florin
'''
from domain.entities import create_student
def test_create_student():
    student = create_student("miie1234","Johnyy","Alba Iulia",10)
    
    assert student["code"]=="miie1234" and student["name"]=="Johnyy" and student["hometown"]=="Alba Iulia" and student["grade"]==10

