import unittest
from repository.repository import Repository
from domain.validators import ParticipationValidator, ActivityValidator, PersonValidator
from controller.participation_controller import ParticipationController, ParticipationControllerException
from util.common import Common
from controller.activity_controller import ActivityController
from controller.person_controller import PersonController
from _datetime import datetime

class TestParticipationController(unittest.TestCase):
    def setUp(self):
        self.person_repository = Repository(PersonValidator)
        self.person_controller = PersonController(self.person_repository)

        self.activity_repository = Repository(ActivityValidator)
        self.activity_controller = ActivityController(self.activity_repository)

        self.repository = Repository(ParticipationValidator)
        self.controller = ParticipationController(self.repository,self.person_controller,self.activity_controller)

        # add test data
        self.person_controller.add(1,"John","1234567890","street 1")
        self.person_controller.add(2,"John","1234567890","street 1")
        self.person_controller.add(3,"John","1234567890","street 1")

        self.activity_controller.add(1,Common.convert_to_date("15.11.2016"),Common.convert_to_time("06:03"),"description")
        self.activity_controller.add(2,Common.convert_to_date("16.11.2016"),Common.convert_to_time("06:03"),"description")

        return super().setUp()

    def test_add(self):
        """Test the add function."""
        self.controller.add(1,1,1)
        self.assertEqual(len(self.controller.get_all()),1,"Repository size should be 1")

        self.assertRaises(ParticipationControllerException,self.controller.add,2,4,2)
        self.assertRaises(ParticipationControllerException,self.controller.add,2,1,5)

    def test_remove(self):
        """Test the remove function."""
        self.controller.add(1,1,1)
        self.controller.remove(1)
        self.assertEqual(len(self.controller.get_all()),0,"Repository size should be 0")

    def test_update(self):
        """Test the update function."""
        self.controller.add(1,1,1)
        self.controller.update(1,2,2)
        participation = self.controller.find_by_id(1)
        self.assertEqual(participation.entity_id,1,"Participation id should be 1.")
        self.assertEqual(participation.person_id,2,"Person id should be 2.")
        self.assertEqual(participation.activity_id,2,"Activity id should be 2.")

    def test_get_all(self):
        """Test the get_all function."""
        self.controller.add(1,1,1)
        self.assertEqual(len(self.controller.get_all()),1,"get_all() size should be 1.")

    def find_by_id(self):
        """Test the find_by_id function."""
        self.controller.add(1,1,1)

        participation = self.controller.find_by_id(1)

        self.assertEqual(participation.entity_id,1,"Participation id should be 1.")
        self.assertEqual(participation.person_id,1,"Person id should be 1.")
        self.assertEqual(participation.activity_id,1,"Activity id should be 1.")

    def test_find_by_activity_id(self):
        """Test the find_by_activity id function."""
        self.controller.add(1,1,1)

        participation = self.controller.find_by_activity_id(1)
        self.assertEqual(participation[0].entity_id,1,"Participation id should be 1.")
        self.assertEqual(participation[0].person_id,1,"Person id should be 1.")
        self.assertEqual(participation[0].activity_id,1,"Activity id should be 1.")
    
    def test_find_by_person_id(self):
        """Test the find_by_person_id function."""
        self.controller.add(1,1,1)

        participation = self.controller.find_by_person_id(1)
        self.assertEqual(participation[0].entity_id,1,"Participation id should be 1.")
        self.assertEqual(participation[0].person_id,1,"Person id should be 1.")
        self.assertEqual(participation[0].activity_id,1,"Activity id should be 1.")

    def test_find_by_activity_time(self):
        """Test the find by activity time function."""
        self.controller.add(1,1,1)

        participation = self.controller.find_by_activity_time(Common.convert_to_time("06:03"))
        self.assertEqual(participation[0].entity_id,1,"Participation id should be 1.")
        self.assertEqual(participation[0].person_id,1,"Person id should be 1.")
        self.assertEqual(participation[0].activity_id,1,"Activity id should be 1.")

    def test_find_by_activity_date(self):
        """Test the find by activity date function."""
        self.controller.add(1,1,1)

        participation = self.controller.find_by_activity_date(Common.convert_to_date("15.11.2016"))
        self.assertEqual(participation[0].entity_id,1,"Participation id should be 1.")
        self.assertEqual(participation[0].person_id,1,"Person id should be 1.")
        self.assertEqual(participation[0].activity_id,1,"Activity id should be 1.")

    def test_find_by_activity_description(self):
        """Test the find by activity description function."""
        self.controller.add(1,1,1)

        participation = self.controller.find_by_activity_description("description")
        self.assertEqual(participation[0].entity_id,1,"Participation id should be 1.")
        self.assertEqual(participation[0].person_id,1,"Person id should be 1.")
        self.assertEqual(participation[0].activity_id,1,"Activity id should be 1.")

    def test_statistics_activity_by_day(self):
        """Test the statistics_activity_by_day function."""
        self.controller.add(1,1,1)

        participation = self.controller.statistics_activity_by_day(15)
        self.assertEqual(participation[0].entity_id,1,"Participation id should be 1.")
        self.assertEqual(participation[0].person_id,1,"Person id should be 1.")
        self.assertEqual(participation[0].activity_id,1,"Activity id should be 1.")

    def test_statistics_activity_by_person(self):
        """Test the statistics_activity_by_person function."""
        self.controller.add(1,1,1)

        participation = self.controller.statistics_activity_by_person(1)
        self.assertEqual(participation[0].entity_id,1,"Participation id should be 1.")
        self.assertEqual(participation[0].person_id,1,"Person id should be 1.")
        self.assertEqual(participation[0].activity_id,1,"Activity id should be 1.")

    def test_statistics_activity_by_week(self):
        """Test the statistics_activity_by_person function."""
        self.controller.add(1,1,1)

        participation = self.controller.statistics_activity_by_week(1)
        self.assertEqual(participation[0].entity_id,1,"Participation id should be 1.")
        self.assertEqual(participation[0].person_id,1,"Person id should be 1.")
        self.assertEqual(participation[0].activity_id,1,"Activity id should be 1.")

    def test_delete_by_activity_id(self):
        """Test the delete_by_activity id function."""
        self.controller.add(1,1,1)
        self.controller.delete_by_activity_id(1)

        self.assertEqual(len(self.controller.get_all()),0,"size of get_all() should be 0")

    def test_delete_by_person_id(self):
        """Test the delete_by_person_id function."""
        self.controller.add(1,1,1)
        self.controller.delete_by_person_id(1)
        self.assertEqual(len(self.controller.get_all()),0,"size of get_all() should be 0")

    def test_statistics_sorted_busiest(self):
        """Test the statistics_sorted_busiest function."""
        self.controller.add(1,1,1)

        self.assertEqual(self.controller.statistics_sorted_busiest()[0],Common.convert_to_date("16.11.2016"),"Date should be 16.11.2016")

    def test_statistics_sorted_persons(self):
        """Test the statistics_sorted_persons function."""
        self.controller.add(1,1,1)
        self.assertEqual(self.controller.statistics_sorted_persons()[0].entity_id,1,"Person id should be 1.")

if __name__ == '__main__':
    unittest.main()
