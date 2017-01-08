from util.common import Common
import datetime
from controller.call_stack import CallStack
from controller.call_stack import UndoHandlers
from domain.entities import Person
from domain.entities import Activity

class Console(object):
    """Console based user interface."""
    def __init__(self,person_controller,activity_controller,participation_controller):
        self.__person_controller = person_controller
        self.__activity_controller = activity_controller
        self.__participation_controller = participation_controller
      
    def add_person(self):
        person_id = input("person id:")

        if not Common.get_type(person_id) is int:
            raise ValueError("Person id must be an integer.")

        person_id = int(person_id)

        name = input("name:")

        phone_number = input("phone number:")

        address = input("address:")

        CallStack.add_undo_operation(UndoHandlers.ADD_PERSON_HANDLER,self.__person_controller,Person(person_id,name,phone_number,address)) 

        self.__person_controller.add(person_id,name,phone_number,address)

    def remove_person(self):
        person_id = input("person id:")

        if not Common.get_type(person_id) is int:
            raise ValueError("Person id must be an integer.")

        person_id = int(person_id)
        
        CallStack.add_undo_operation(UndoHandlers.DELETE_PERSON_HANDLER,self.__person_controller,self.__person_controller.find_by_id(person_id),self.__participation_controller,self.__participation_controller.find_by_person_id(person_id))

        self.__person_controller.remove(person_id)
        # also delete the participations for this person
        self.__participation_controller.delete_by_person_id(person_id)
        #self.__participation_controller.delete_person_and_participations(person_id)
        
    def update_person(self):
        person_id = input("person id:")

        if not Common.get_type(person_id) is int:
            raise ValueError("Person id must be an integer.")

        person_id = int(person_id)

        name = input("name:")

        phone_number = input("phone number:")

        address = input("address:")

        CallStack.add_undo_operation(UndoHandlers.UPDATE_PERSON_HANDLER,self.__person_controller,self.__person_controller.find_by_id(person_id))
        
        self.__person_controller.update(person_id,name,phone_number,address)
    
    def list_persons(self):
        Common.print_iterable(self.__person_controller.get_all())     
        
    def add_activity(self):
        activity_id = input("activity id:")
        
        if not Common.get_type(activity_id) is int:
            raise ValueError("Activity id must be an integer.")
        
        activity_id = int(activity_id)
        
        date = input("date:")
        
        if not Common.get_type(date) is datetime.date:
            raise ValueError("Activity date must have the format day.month.year.")  
        
        date = Common.convert_to_date(date)
        
        time = input("time:")
        
        if not Common.get_type(time) is datetime.time:
            raise ValueError("Activity time must have the format hour:minute.")

        time = Common.convert_to_time(time)

        description = input("description:")

        CallStack.add_undo_operation(UndoHandlers.ADD_ACTIVITY_HANDLER,self.__activity_controller,Activity(activity_id,date,time,description))

        self.__activity_controller.add(activity_id,date,time,description)

    def remove_activity(self):
        activity_id = input("activity id:")

        if not Common.get_type(activity_id) is int:
            raise ValueError("Activity id must be an integer.")

        activity_id = int(activity_id)

        CallStack.add_undo_operation(UndoHandlers.DELETE_ACTIVITY_HANDLER,self.__activity_controller,self.__activity_controller.find_by_id(activity_id),self.__participation_controller,self.__participation_controller.find_by_activity_id(activity_id))
        
        # remove the activity
        self.__activity_controller.remove(activity_id)

        # we can also remove the participations that have this activity
        self.__participation_controller.delete_by_activity_id(activity_id)

        #self.__participation_controller.delete_activity_and_participations(activity_id)

    def update_activity(self):
        activity_id = input("activity id:")
        
        if not Common.get_type(activity_id) is int:
            raise ValueError("Activity id must be an integer.")
        
        activity_id = int(activity_id)
        
        date = input("date:")
        
        if not Common.get_type(date) is datetime.date:
            raise ValueError("Activity date must have the format day.month.year.")  
        
        date = Common.convert_to_date(date)
        
        time = input("time:")
        
        if not Common.get_type(time) is datetime.time:
            raise ValueError("Activity time must have the format hour:minute.")

        time = Common.convert_to_time(time)

        description = input("description:")     
        
        CallStack.add_undo_operation(UndoHandlers.UPDATE_ACTIVITY_HANDLER,self.__activity_controller,self.__activity_controller.find_by_id(activity_id))

        self.__activity_controller.update(activity_id,date,time,description)

    def list_activities(self):
        Common.print_iterable(self.__activity_controller.get_all())

    def add_participation(self):
        participation_id = input("participation id:")

        if not Common.get_type(participation_id) is int:
            raise ValueError("Participation id must be an integer.")

        participation_id = int(participation_id)

        person_id = input("person_id:")

        if not Common.get_type(person_id) is int:
            raise ValueError("Person id must be an integer.")

        person_id = int(person_id)

        activity_id = input("activity id:")

        if not Common.get_type(activity_id) is int:
            raise ValueError("Activity id must be an integer.")
        
        activity_id = int(activity_id)

        CallStack.add_undo_operation(UndoHandlers.ADD_PARTICIPATION_HANDLER,self.__participation_controller,self.__participation_controller.find_by_id(participation_id))

        self.__participation_controller.add(participation_id,person_id,activity_id)

    def remove_participation(self):
        participation_id = input("participation id:")

        if not Common.get_type(participation_id) is int:
            raise ValueError("Participation id must be an integer.")

        participation_id = int(participation_id)

        CallStack.add_undo_operation(UndoHandlers.DELETE_PARTICIPATION_HANDLER,self.__participation_controller,self.__participation_controller.find_by_id(participation_id))

        self.__participation_controller.remove(participation_id)

    def update_participation(self):
        participation_id = input("participation id:")

        if not Common.get_type(participation_id) is int:
            raise ValueError("Participation id must be an integer.")

        participation_id = int(participation_id)

        person_id = input("person_id:")

        if not Common.get_type(person_id) is int:
            raise ValueError("Person id must be an integer.")

        person_id = int(person_id)

        activity_id = input("activity id:")

        if not Common.get_type(activity_id) is int:
            raise ValueError("Activity id must be an integer.")
        
        activity_id = int(activity_id)

        CallStack.add_undo_operation(UndoHandlers.UPDATE_PARTICIPATION_HANDLER,self.__participation_controller,self.__participation_controller.find_by_id(participation_id))

        self.__participation_controller.update(participation_id,person_id,activity_id)

    def print_participations(self,participations):
        for p in participations:
            print(p,self.__activity_controller.find_by_id(p.activity_id))

    def list_participations(self):
        self.print_participations(self.__participation_controller.get_all())

    def search_person_by_phone_number(self):
        phone_number = input("phone number:")

        Common.print_iterable(self.__person_controller.find_by_phone_number(phone_number))

    def search_person_by_name(self):
        name = input("name:")

        Common.print_iterable(self.__person_controller.find_by_name(name))

    def search_participation_by_date(self):
        date = input("date:")
        
        if not Common.get_type(date) is datetime.date:
            raise ValueError("Activity date must have the format day.month.year.")  

        date=Common.convert_to_date(date)
        self.print_participations(self.__participation_controller.find_by_activity_date(date))

    def search_participation_by_time(self):
        time = input("time:")
        
        if not Common.get_type(time) is datetime.time:
            raise ValueError("Activity time must have the format hour:minute.")

        time = Common.convert_to_time(time)
        self.print_participations(self.__participation_controller.find_by_activity_time(time))

    def search_participation_by_description(self):
        description = input("description:")
        self.print_participations(self.__participation_controller.find_by_activity_description(description))
    
    def statistics_participation_day(self):
        day = input("day:")

        if not Common.get_type(day) is int:
            raise ValueError("Day value must be an integer.")

        day = int(day)
        self.print_participations(self.__participation_controller.statistics_activity_by_day(day))

    def statistics_participation_week(self):
        week = input("week:")

        if not Common.get_type(week) is int:
            raise ValueError("Day value must be an integer.")

        week = int(week)
        self.print_participations(self.__participation_controller.statistics_activity_by_week(week))

    def statistics_participation_busiest(self):
        Common.print_iterable(self.__participation_controller.statistics_sorted_busiest())

    def statistics_participation_person(self):
        person_id = input("person id:")

        if not Common.get_type(person_id) is int:
            raise ValueError("Person id must be an integer.")

        person_id = int(person_id)
        self.print_participations(self.__participation_controller.statistics_activity_by_person(person_id))
    
    def list_persons_sorted_participations(self):
        Common.print_iterable(self.__participation_controller.statistics_sorted_persons())         

    def print_menu(self):
        print("1.add a person")
        print("2.remove a person")
        print("3.update person")
        print("4.list persons")
        print("5.add activity")
        print("6.remove activity")
        print("7.update activity")
        print("8.list activities")
        print("9.add participation")
        print("10.remove participation")
        print("11.update participation")
        print("12.list participations")
        print("13.search person by name")
        print("14.search person by phone number")
        print("15.search participation by date")
        print("16.search participation by time")
        print("17.search participation by description")
        print("18.statistics participation by day")
        print("19.statistics participation by week")
        print("20.statistics participation busiest")
        print("21.statistics participation person")
        print("22.statistics participation persons")
        print("23.undo")
        print("24.redo")

    def read_command_index(self):
        cmd_index = input("command:")

        if not Common.get_type(cmd_index) is int:
            raise ValueError("Command must be an integer.")

        return int(cmd_index)

    def run(self):
        commands = {1:self.add_person,2:self.remove_person,3:self.update_person,4:self.list_persons,5:self.add_activity,6:self.remove_activity,
                    7:self.update_activity,8:self.list_activities,9:self.add_participation,10:self.remove_participation,11:self.update_participation,12:self.list_participations,
                    13:self.search_person_by_name,14:self.search_person_by_phone_number,15:self.search_participation_by_date,16:self.search_participation_by_time,
                    17:self.search_participation_by_description,18:self.statistics_participation_day,19:self.statistics_participation_week,
                    20:self.statistics_participation_busiest,21:self.statistics_participation_person,22:self.list_persons_sorted_participations,
                    23:CallStack.undo,24:CallStack.redo
                    }
        
        self.print_menu()

        while True:
            cmd_index = self.read_command_index()

            if cmd_index==len(commands)+1:
                break

            if cmd_index<1 or cmd_index>len(commands):
                print("No command with id {0} exists.".format(cmd_index))
            #try:
            commands[cmd_index]()
            #except Exception as ex:
                #print(ex)
