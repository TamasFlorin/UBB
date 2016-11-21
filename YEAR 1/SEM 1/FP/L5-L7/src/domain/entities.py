from util.common import Common
from _collections import OrderedDict
import inspect

class Person(object):
    def __init__(self,person_id,name,phone_number,address):
        self.__person_id = person_id
        self.__name = name
        self.__phone_number = phone_number
        self.__address = address

    @property
    def entity_id(self):
        return self.__person_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        self.__name = value
    
    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self,value):
        self.__phone_number = value

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self,value):
        self.__address = value

    def __str__(self):
        return "id:{0} name:{1} phone number:{2} address:{3}".format(self.__person_id,self.__name,self.__phone_number,self.__address)

    def __eq__(self,other):
        return self.__person_id==other.entity_id

    def __ne__(self):
        return not self.__eq__(other)

class Activity(object):
    def __init__(self,activity_id,date,time,description):
        self.__activity_id = activity_id
        self.__date = date
        self.__time = time
        self.__description = description
        
    @property
    def entity_id(self):
        return self.__activity_id

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self,value):
        self.__date = value
    
    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self,value):
        self.__time = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self,value):
        self.__description = value

    def __str__(self):
        return "activity_id={0} date={1} time={2} description={3}".format(self.__activity_id,self.__date,self.__time,self.__description)

    def __eq__(self,other):
        return self.__activity_id==other.entity_id

    def __ne__(self):
        return not self.__eq__(other)

class Participation:
    """Class used to link the person with the activity."""
    def __init__(self,participation_id,person_id,activity_id):
        self.__participation_id = participation_id
        self.__person_id = person_id
        self.__activity_id = activity_id

    @property
    def entity_id(self):
        return self.__participation_id

    @property
    def person_id(self):
        return self.__person_id

    @property
    def activity_id(self):
        return self.__activity_id

    def __str__(self):
        return "participation id={0} person id={1}".format(self.__participation_id,self.__person_id)

    def __eq__(self,other):
        return self.__participation_id==other.entity_id

    def __ne__(self):
        return not self.__eq__(other)