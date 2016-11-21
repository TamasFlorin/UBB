from domain.entities import Person

class PersonController(object):
    def __init__(self,person_repository):
        """Initialize the person repository."""
        self.__person_repository = person_repository

    def add(self,id:int,name:str,phone_number:str,address:str):
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

    def remove(self,id:int):
        """Remove a person entity from the person repository.
        Args:
            id(uint): the id of the person to be removed
        Returns:
            None
        """
        self.__person_repository.delete_by_id(id)

    def update(self,id:int,name:str,phone_number:str,address:str):
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

    def find_by_id(self,person_id:int):
        """Find a person entity in the repository matching a given id.
        Args:
            person_id(uint): the id of the person to be found
        Returns:
            the person object matching the given id.
        """
        return self.__person_repository.find_by_id(person_id)

    def find_by_name(self,name:str):
        """Find a person entity in the repository matching a given name.
        Args:
            name(str): the name of the person to be found
        Returns:
            the person object matching the given name.
        """
        return list(filter(lambda x: name.lower() in x.name.lower(),self.get_all()))

    def find_by_phone_number(self,phone_number:str):
        """Find a person entity in the repository matching a given phone number.
        Args:
            phone_number(str): the phone number of the person to be found
        Returns:
            the person object matching the given phone number.
        """
        return list(filter(lambda x: phone_number in x.phone_number,self.get_all()))
