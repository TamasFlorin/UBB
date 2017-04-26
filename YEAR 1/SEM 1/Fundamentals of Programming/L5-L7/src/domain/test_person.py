import unittest
from domain.entities import Person

class TestPerson(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.__person = Person(1,"Johny","0756705316","street nr1")

    def test_entity_id(self):
        self.assertEqual(self.__person.entity_id,1,"person entity id should be 1")

    def test_name(self):
        self.assertEqual(self.__person.name,"Johny","person name should be 'Johny'")

    def test_phone_number(self):
        self.assertEqual(self.__person.phone_number,"0756705316","person phone number should be '0756705316'")

    def test_address(self):
        self.assertEqual(self.__person.address,"street nr1","person address should be 'street nr 1'")

    def test_eq(self):
        self.assertFalse(self.__person==Person(2,"lol","0000000000","street nr 2"),"Persons should not be equal.")

if __name__ == '__main__':
    unittest.main()
