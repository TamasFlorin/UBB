from util.common import Common
import datetime
from domain.command import Command
import sys

class Console(object):
    """Console based user interface."""
    def __init__(self,person_controller,activity_controller,participation_controller):
        self.__person_controller = person_controller
        self.__activity_controller = activity_controller
        self.__participation_controller = participation_controller

    def read_command_index(self):
        cmd_index = input("command:")

        if not Common.get_type(cmd_index) is int:
            raise ValueError("Command index must be an integer.")

        return int(cmd_index)

    def execute_command(self,command:Command):
        raw_input = []
        count = 0

        # read the needed arguments in order to execute the command
        for func_name,args in command.arguments.items():
            raw_input.append([])
            for arg in args:
                raw_input[count].append(input(arg.name+":"))
            count += 1

        if len(raw_input)>1:
            return command.execute(raw_input[0],raw_input[1])

        return command.execute(raw_input[0])

    def print_commands(self,commands):
        for key in commands:
            print("{0}.{1}".format(key,commands[key].name))

    def print_participations(self,participations:list):
        for p in participations:
            print(p,self.__activity_controller.find_by_id(p.activity_id))

    def exit(self):
        raise SystemExit

    def load_predefinded_data(self):
        self.__person_controller.add(1,"John0","1234567890","str1")
        self.__person_controller.add(2,"John1","1234567890","str1")
        self.__person_controller.add(3,"John2","1234567890","str1")

        self.__activity_controller.add(1,Common.convert_to_date("15.11.2016"),Common.convert_to_time("06:03"),"description")
        self.__activity_controller.add(2,Common.convert_to_date("16.11.2016"),Common.convert_to_time("06:03"),"description")
        self.__activity_controller.add(3,Common.convert_to_date("16.11.2016"),Common.convert_to_time("06:04"),"description")
        self.__activity_controller.add(4,Common.convert_to_date("16.11.2016"),Common.convert_to_time("06:06"),"description")
        self.__activity_controller.add(5,Common.convert_to_date("16.11.2016"),Common.convert_to_time("06:07"),"description")
        self.__activity_controller.add(6,Common.convert_to_date("23.11.2016"),Common.convert_to_time("06:07"),"description")

        self.__participation_controller.add(1,1,1)
        self.__participation_controller.add(2,2,1)
        self.__participation_controller.add(3,1,2)
        self.__participation_controller.add(4,1,2)
        self.__participation_controller.add(5,3,2)
        self.__participation_controller.add(6,3,6)

    def run(self):
        commands = {1:Command("add person",self.__person_controller.add),
                    2:Command("remove person",self.__participation_controller.delete_person),
                    3:Command("update person",self.__person_controller.update),
                    4:Command("list persons",Common.print_iterable,"iterable",arg=self.__person_controller.get_all),
                    5:Command("add activity",self.__activity_controller.add),
                    6:Command("remove activity",self.__participation_controller.delete_activity),
                    7:Command("update activity",self.__activity_controller.update),
                    8:Command("list activities",Common.print_iterable,"iterable",arg=self.__activity_controller.get_all),
                    9:Command("add participation",self.__participation_controller.add),
                    10:Command("remove participation",self.__participation_controller.remove),
                    11:Command("update participation",self.__participation_controller.update),
                    12:Command("list participations",self.print_participations,"participations",arg=self.__participation_controller.get_all),
                    13:Command("search person by name",Common.print_iterable,"iterable",arg=self.__person_controller.find_by_name),
                    14:Command("search person by phone number",Common.print_iterable,"iterable",arg=self.__person_controller.find_by_phone_number),
                    15:Command("search participation by date",self.print_participations,"participations",arg=self.__participation_controller.find_by_activity_date),
                    16:Command("search participation by time",self.print_participations,"participations",arg=self.__participation_controller.find_by_activity_time),
                    17:Command("search participation by description",self.print_participations,"participations",arg=self.__participation_controller.find_by_activity_description),
                    18:Command("statistics participation by day",self.print_participations,"participations",arg=self.__participation_controller.statistics_activity_by_day),
                    19:Command("statistics participation by week",self.print_participations,"participations",arg=self.__participation_controller.statistics_activity_by_week),
                    20:Command("statistics participation busiest",Common.print_iterable,"iterable",arg=self.__participation_controller.statistics_sorted_busiest),
                    21:Command("statistics participation persons",Common.print_iterable,"iterable",arg=self.__participation_controller.statistics_sorted_persons),
                    22:Command("exit",self.exit)
                    }
        
        self.load_predefinded_data()
        self.print_commands(commands)

        while True:
            try:
                cmd_index = self.read_command_index()

                if cmd_index<1 or cmd_index>len(commands):
                    print("No command with id {0} exists.".format(cmd_index))

                self.execute_command(commands[cmd_index])
            except Exception as ex:
                print(ex)