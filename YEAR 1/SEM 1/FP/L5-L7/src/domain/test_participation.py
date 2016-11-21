import unittest
from domain.Entities import Participation

class TestParticipation(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.__participation = Participation(1,1,1)

    def test_entity_id(self):
        self.assertEqual(self.__participation.entity_id,1,"participation entity id should be 1")

    def test_person_id(self):
        self.assertEqual(self.__participation.person_id,1,"participation person id should be 1")

    def test_activity_id(self):
        self.assertEqual(self.__participation.activity_id,1,"participation activity id should be 1")

if __name__ == '__main__':
    unittest.main()
