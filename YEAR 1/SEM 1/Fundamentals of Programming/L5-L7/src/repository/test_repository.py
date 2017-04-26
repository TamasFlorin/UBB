import unittest
from repository.repository import Repository, RepositoryException, DuplicateIdException, IdNotFoundException
from domain.validators import PersonValidator
from domain.entities import Person

class TestRepository(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.__repository = Repository(PersonValidator)

    def test_find_by_id(self):
        p = Person(1,"John","0756705316","street 1")
        self.__repository.save(p)

        self.assertEqual(self.__repository.find_by_id(1),p,"find_by_id(1) should be equal to p")
        self.assertEqual(self.__repository.find_by_id(2),None,"find_by_id(2) should be equal to None")

    def test_save(self):
        p = Person(1,"John","0756705316","street 1")
        self.__repository.save(p)

        # check if the size of the repository has changed
        self.assertEqual(len(self.__repository.get_all()),1,"repository length should be 1")

        p2 = Person(1,"John1","0756705415","street 2")

        # check for DuplicateIdException
        self.assertRaises(DuplicateIdException,self.__repository.save,p2)

        # check for ValidatorException
        p3 = Person("invalid",123,"00",12)
        self.assertRaises(RepositoryException,self.__repository.save,p3)

    def test_update(self):
        p = Person(1,"John","0756705316","street 1")
        self.__repository.save(p)

        p2 = Person(1,"John1","0000000000","street2")
        self.__repository.update(p2)

        self.assertEqual(self.__repository.find_by_id(1),p2,"find_by_id(1) should be equal to p2")

        p3 = Person("Invalid",12341,131,131)
        self.assertRaises(RepositoryException,self.__repository.update,p3)

        p4 = Person(5,"Inexistent","0000000000","street 5")

        self.assertRaises(IdNotFoundException,self.__repository.update,p4)


    def test_delete_by_id(self):
        p = Person(1,"John","0756705316","street 1")
        self.__repository.save(p)

        self.__repository.delete_by_id(p.entity_id)

        self.assertEqual(len(self.__repository.get_all()),0,"repository size should be 0")

        self.assertRaises(IdNotFoundException,self.__repository.delete_by_id,100)

    def test_get_all(self):
        p = Person(1,"John","0756705316","street 1")
        self.__repository.save(p)

        self.assertEqual(len(self.__repository.get_all()),1,"repository size should be 1")

if __name__ == '__main__':
    unittest.main()
