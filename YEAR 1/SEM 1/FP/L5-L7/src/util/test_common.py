import unittest
from util.common import Common
from _datetime import datetime,date,time

class TestCommon(unittest.TestCase):
    def test_convert_to_date(self):
        self.assertEqual(Common.convert_to_date("19.11.2016"),datetime.strptime("19.11.2016","%d.%m.%Y").date(),"date convert should be equal")

    def test_convert_to_time(self):
        self.assertEqual(Common.convert_to_time("15:46"),datetime.strptime("15:46","%H:%M").time(),"time convert should be equal")

    def test_get_type(self):
        self.assertEqual(Common.get_type("string"),str,"get_type('string') should be str")
        self.assertEqual(Common.get_type("123"),int,"get_type('123') should be int")
        self.assertEqual(Common.get_type("1.2"),float,"get_type('1.2') should be float")
        self.assertEqual(Common.get_type("19.11.2016"),date,"get_type('19.11.2016') should be date")
        self.assertEqual(Common.get_type("15:50"),time,"get_type('15:50') should be time")
        self.assertEqual(Common.get_type("123abcd:"),str,"get_type('123abcd:') should be str")

if __name__ == '__main__':
    unittest.main()
