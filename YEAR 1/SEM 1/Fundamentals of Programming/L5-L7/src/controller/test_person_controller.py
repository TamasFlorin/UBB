import unittest
from repository.repository import Repository
from domain.validators import PersonValidator
from controller.person_controller import PersonController
from domain.entities import Person

class TestPersonController(unittest.TestCase):
    def setUp(self):
        self.__person_repository = Repository(PersonValidator)
        self.__controller = PersonController(self.__person_repository)
        return super().setUp()

    def test_add(self):
        """Test the add function."""
        person = Person(1,"John","1234567890","street 1")

        self.__controller.add(person.entity_id,person.name,person.phone_number,person.address)

        self.assertEqual(len(self.__controller.get_all()),1,"Repository size should now be 1.")

    def test_remove(self):
        """Test the remove function."""
        person = Person(1,"John","1234567890","street 1")

        self.__controller.add(person.entity_id,person.name,person.phone_number,person.address)

        self.__controller.remove(person.entity_id)
        
        self.assertEqual(len(self.__controller.get_all()),0,"Repository size should now be 0.")

    def test_update(self):
        """Test the update function."""
        person = Person(1,"John","1234567890","street 1")

        self.__controller.add(person.entity_id,person.name,person.phone_number,person.address)

        self.__controller.update(person.entity_id,"Jimmy","0123456789","street new")

        self.assertEqual(self.__controller.find_by_id(1).name,"Jimmy","Person name should be Jimmy")
        self.assertEqual(self.__controller.find_by_id(1).phone_number,"0123456789","Person phone number should be 0123456789")
        self.assertEqual(self.__controller.find_by_id(1).address,"street new","Person street should be street new")

    def test_find_by_id(self):
        """Test the find_by_id function."""
        person = Person(1,"John","1234567890","street 1")

        self.__controller.add(person.entity_id,person.name,person.phone_number,person.address)

        person = self.__controller.find_by_id(1)

        self.assertEqual(person.entity_id,1,"Person entity id should be 1")
        self.assertEqual(person.name,"John","Person name should be John")
        self.assertEqual(person.phone_number,"1234567890","Person phone number should be 1234567890")
        self.assertEqual(person.address,"street 1","Person street address should be street 1")

    def test_find_by_name(self):
        """Test the find_by_name function."""
        person = Person(1,"John","1234567890","street 1")

        self.__controller.add(person.entity_id,person.name,person.phone_number,person.address)

        persons = self.__controller.find_by_name("Jo") # partial string matching

        self.assertEqual(len(persons),1,"Persons size should be 1.")

        self.assertEqual(persons[0].entity_id,1,"Person entity id should be 1")
        self.assertEqual(persons[0].name,"John","Person name should be John")
        self.assertEqual(persons[0].phone_number,"1234567890","Person phone number should be 1234567890")
        self.assertEqual(persons[0].address,"street 1","Person street address should be street 1")

    def test_find_by_phone_number(self):
        """Test the find_by_phone_number function."""
        person = Person(1,"John","1234567890","street 1")

        self.__controller.add(person.entity_id,person.name,person.phone_number,person.address)

        persons = self.__controller.find_by_phone_number("12345") # partial string matching

        self.assertEqual(len(persons),1,"Persons size should be 1.")

        self.assertEqual(persons[0].entity_id,1,"Person entity id should be 1")
        self.assertEqual(persons[0].name,"John","Person name should be John")
        self.assertEqual(persons[0].phone_number,"1234567890","Person phone number should be 1234567890")
        self.assertEqual(persons[0].address,"street 1","Person street address should be street 1")

if __name__ == '__main__':
    unittest.main()
