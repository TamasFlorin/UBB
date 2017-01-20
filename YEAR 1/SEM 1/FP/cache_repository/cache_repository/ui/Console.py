class Console(object):
    def __init__(self,simple_controller):
        self.__controller = simple_controller

    def save_entity(self):
        id = int(input('id='))
        name = input('name=')
        age = int(input('age='))

        self.__controller.add(id,name,age)

    def find_entity(self):
        id = int(input("id="))
        print(self.__controller.find_by_id(id))

    def print_all(self):
        for entity in self.__controller.get_all():
            print(entity)

    def print_menu(self):
        print("0.Save entity.")
        print("1.Find entity.")
        print("2.Print entities from file.")

    def run(self):
        commands = {0:self.save_entity,1:self.find_entity,2:self.print_all }
        self.print_menu()
        while True:
            command = int(input('command='))

            if command >=0 and command <len(commands):
                commands[command]()




