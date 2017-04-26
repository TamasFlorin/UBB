import unittest
from repository.repository import Repository
from domain.validators import ActivityValidator
from controller.activity_controller import ActivityController, ActivityControllerException
from util.common import Common

class TestActivityController(unittest.TestCase):
    def setUp(self):
        """Set up the test object."""
        self.activity_repository = Repository(ActivityValidator)
        self.controller = ActivityController(self.activity_repository)

        return super().setUp()

    def test_add(self):
        """Test the add function."""
        self.controller.add(1,Common.convert_to_date("19.11.2016"),Common.convert_to_time("17:14"),"description")

        self.assertEqual(len(self.controller.get_all()),1,"Activity repository size should be 1")

        self.assertRaises(ActivityControllerException,self.controller.add,2,Common.convert_to_date("19.11.2016"),Common.convert_to_time("17:14"),"description")

    def test_remove(self):
        """Test the remove function."""
        self.controller.add(1,Common.convert_to_date("19.11.2016"),Common.convert_to_time("17:14"),"description")
        self.controller.remove(1)

        self.assertEqual(len(self.controller.get_all()),0,"Repository size should be 0.")

    def test_update(self):
        """Test the update function."""
        self.controller.add(1,Common.convert_to_date("19.11.2016"),Common.convert_to_time("17:14"),"description")
        self.controller.update(1,Common.convert_to_date("20.11.2016"),Common.convert_to_time("19:15"),"description new")

        activity = self.controller.find_by_id(1)

        self.assertEqual(activity.entity_id,1,"Activity id should be 1")
        self.assertEqual(activity.date,Common.convert_to_date("20.11.2016"),"Activity date should be 20.11.2016")
        self.assertEqual(activity.time,Common.convert_to_time("19:15"),"Activity time should be 19:15")
        self.assertEqual(activity.description,"description new","Activity description should be 'description new'")

    def test_get_all(self):
        """Test the get_all function."""
        self.controller.add(1,Common.convert_to_date("19.11.2016"),Common.convert_to_time("17:14"),"description")
        self.assertEqual(len(self.controller.get_all()),1,"get_all() result size should be 1")

    def test_find_by_id(self):
        """Test the find_by_id functions."""
        self.controller.add(1,Common.convert_to_date("19.11.2016"),Common.convert_to_time("17:14"),"description")
        activity = self.controller.find_by_id(1)
        self.assertEqual(activity.entity_id,1,"Activity id should be 1")
        self.assertEqual(activity.date,Common.convert_to_date("19.11.2016"),"Activity date should be 19.11.2016")
        self.assertEqual(activity.time,Common.convert_to_time("17:14"),"Activity time should be 17:14")
        self.assertEqual(activity.description,"description","Activity description should be 'description'")

    def test_find_by_date(self):
        """Test the find by date function."""
        self.controller.add(1,Common.convert_to_date("19.11.2016"),Common.convert_to_time("17:14"),"description")
        activities = self.controller.find_by_date(Common.convert_to_date("19.11.2016"))

        self.assertEqual(len(activities),1,"The size of the activities should be 1.")
        self.assertEqual(activities[0].entity_id,1,"Activity id should be 1")
        self.assertEqual(activities[0].date,Common.convert_to_date("19.11.2016"),"Activity date should be 19.11.2016")
        self.assertEqual(activities[0].time,Common.convert_to_time("17:14"),"Activity time should be 17:14")
        self.assertEqual(activities[0].description,"description","Activity description should be 'description'")

    def test_find_by_time(self):
        """Test the find by time function."""
        self.controller.add(1,Common.convert_to_date("19.11.2016"),Common.convert_to_time("17:14"),"description")
        activities = self.controller.find_by_time(Common.convert_to_time("17:14"))

        self.assertEqual(len(activities),1,"The size of the activities should be 1.")
        self.assertEqual(activities[0].entity_id,1,"Activity id should be 1")
        self.assertEqual(activities[0].date,Common.convert_to_date("19.11.2016"),"Activity date should be 19.11.2016")
        self.assertEqual(activities[0].time,Common.convert_to_time("17:14"),"Activity time should be 17:14")
        self.assertEqual(activities[0].description,"description","Activity description should be 'description'")

    def test_find_by_description(self):
        """Test the find_by_description function."""
        self.controller.add(1,Common.convert_to_date("19.11.2016"),Common.convert_to_time("17:14"),"description")
        activities = self.controller.find_by_description("descr")

        self.assertEqual(len(activities),1,"The size of the activities should be 1.")
        self.assertEqual(activities[0].entity_id,1,"Activity id should be 1")
        self.assertEqual(activities[0].date,Common.convert_to_date("19.11.2016"),"Activity date should be 19.11.2016")
        self.assertEqual(activities[0].time,Common.convert_to_time("17:14"),"Activity time should be 17:14")
        self.assertEqual(activities[0].description,"description","Activity description should be 'description'")

    def test_find_by_day(self):
        """Test the find by day function."""
        self.controller.add(1,Common.convert_to_date("19.11.2016"),Common.convert_to_time("17:14"),"description")
        activities = self.controller.find_by_day(19)

        self.assertEqual(len(activities),1,"The size of the activities should be 1.")
        self.assertEqual(activities[0].entity_id,1,"Activity id should be 1")
        self.assertEqual(activities[0].date,Common.convert_to_date("19.11.2016"),"Activity date should be 19.11.2016")
        self.assertEqual(activities[0].time,Common.convert_to_time("17:14"),"Activity time should be 17:14")
        self.assertEqual(activities[0].description,"description","Activity description should be 'description'")

    def test_compute_week_date(self):
        """Test the compute_week_date function."""
        self.controller.add(1,Common.convert_to_date("1.11.2016"),Common.convert_to_time("17:14"),"description")
        date = self.controller._ActivityController__compute_week_date(2)
        self.assertEqual(date,Common.convert_to_date("15.11.2016"))

    def test_find_by_week(self):
        """Test the find_by_week function."""
        self.controller.add(1,Common.convert_to_date("19.11.2016"),Common.convert_to_time("17:14"),"description")
        activities = self.controller.find_by_week(1)

        self.assertEqual(len(activities),1,"The size of the activities should be 1.")
        self.assertEqual(activities[0].entity_id,1,"Activity id should be 1")
        self.assertEqual(activities[0].date,Common.convert_to_date("19.11.2016"),"Activity date should be 19.11.2016")
        self.assertEqual(activities[0].time,Common.convert_to_time("17:14"),"Activity time should be 17:14")
        self.assertEqual(activities[0].description,"description","Activity description should be 'description'")

        activities = self.controller.find_by_week(2)

        self.assertEqual(len(activities),0,"The size of the activities should be 0.")

if __name__ == '__main__':
    unittest.main()
