import unittest
from domain.entities import Activity
from util.common import Common

class TestActivity(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.__activity = Activity(1,Common.convert_to_date("16.11.2016"),Common.convert_to_time("00:33"),"description")

    def test_entity_id(self):
        # test getter
        self.assertEqual(self.__activity.entity_id,1,"activity entity id should be 1")

    def test_entity_date(self):
        self.assertEqual(self.__activity.date,Common.convert_to_date("16.11.2016"),"activity date should be 16.11.2016")

    def test_entity_time(self):
        self.assertEqual(self.__activity.time,Common.convert_to_time("00:33"),"activity time should be 0:33")

    def test_str(self):
        self.assertEqual(self.__activity.__str__(),"activity_id=1 date=2016-11-16 time=00:33:00 description=description","str representation should match.")

if __name__ == '__main__':
    unittest.main()