from domain.entities import Person
from domain.custom import filter
from domain.custom import sort
class PersonController(object):
    def __init__(self,person_repository):
        """Initialize the person repository."""
        self.__person_repository = person_repository

    @staticmethod
    def read_entity(file_name):
        with open(file_name,'r') as f:
            line = f.read()
            line = line.split(" ")
            entity = Person(int(line[0]),line[1],line[2],line[3])
            return entity

        return None

    @staticmethod
    def write_entity(file_name,entity):
        with open(file_name,'w') as f:
            line = str(entity.entity_id) + " " + entity.name +" "+ entity.phone_number +" "+ entity.address
            f.write(line)

    def add(self,id,name,phone_number,address):
        """Add a new person entity to the person repository.
        Args:
            id(uint): the id of the person
            name(str): the name of the person
            phone_number(str): the phone number of the person
            address(str): the address of the person
        Returns:
            None
            """
        self.__person_repository.save(Person(id,name,phone_number,address))

    def remove(self,id):
        """Remove a person entity from the person repository.
        Args:
            id(uint): the id of the person to be removed
        Returns:
            None
        """
        self.__person_repository.delete_by_id(id)

    def update(self,id,name,phone_number,address):
        """Update a person entity from the reposity.
        Args:
            id(uint): the id of the person entity to be updated
            name(str): the new name of the person
            phone_number(str): the new phone number of the person
            address(str): the new address of the person
        Returns:
            None
        """
        self.__person_repository.update(Person(id,name,phone_number,address))

    def get_all(self):
        """Return the dict list containg all the person entity objects."""
        return self.__person_repository.get_all()

    def find_by_id(self,person_id):
        """Find a person entity in the repository matching a given id.
        Args:
            person_id(uint): the id of the person to be found
        Returns:
            the person object matching the given id.
        """
        return self.__person_repository.find_by_id(person_id)

    def find_by_name(self,name):
        """Find a person entity in the repository matching a given name.
        Args:
            name(str): the name of the person to be found
        Returns:
            the person object matching the given name.
        """
        return list(filter(lambda x: name.lower() in x.name.lower(),self.get_all()))

    def find_by_phone_number(self,phone_number):
        """Find a person entity in the repository matching a given phone number.
        Args:
            phone_number(str): the phone number of the person to be found
        Returns:
            the person object matching the given phone number.
        """
        return list(filter(lambda x: phone_number in x.phone_number,self.get_all()))
        
