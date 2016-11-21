import unittest
from domain.Entities import Person, Activity, Participation
from domain.validators import PersonValidatorException, PersonValidator, ActivityValidatorException, ActivityValidator, ParticipationValidatorException, ParticipationValidator
from util.common import Common

class TestValidators(unittest.TestCase):
    def setUp(self):
        return super().setUp()

    def test_person_validator(self):
        # invalid id check
        person = Person("string","John","0756705316","street 1")
        self.assertRaises(PersonValidatorException,PersonValidator.validate,person)

        person = Person(1,123,"0756705316","street 1")

        self.assertRaises(PersonValidatorException,PersonValidator.validate,person)

        person = Person(1,"John",1234,"street 1")

        self.assertRaises(PersonValidatorException,PersonValidator.validate,person)

        person = Person(1,"John","a123456789","street 1")
        self.assertRaises(PersonValidatorException,PersonValidator.validate,person)

        person = Person(1,"John","0756705316",123)

        self.assertRaises(PersonValidatorException,PersonValidator.validate,person)

    def test_activity_validator(self):
        # check invalid id
        activity = Activity("invalid",Common.convert_to_date("18.11.2016"),Common.convert_to_time("16:47"),"description")

        self.assertRaises(ActivityValidatorException,ActivityValidator.validate,activity)

        # check invalid date
        activity = Activity(1,"invalid",Common.convert_to_time("16:47"),"description")

        self.assertRaises(ActivityValidatorException,ActivityValidator.validate,activity)

        # check invalid time
        activity = Activity(1,Common.convert_to_date("18.11.2016"),"invalid","description")
        self.assertRaises(ActivityValidatorException,ActivityValidator.validate,activity)

        # check invalid description
        activity = Activity(1,Common.convert_to_date("18.11.2016"),Common.convert_to_time("16:47"),123)
        self.assertRaises(ActivityValidatorException,ActivityValidator.validate,activity)

    def test_participation_validator(self):
        participation = Participation("invalid",1,1)
        self.assertRaises(ParticipationValidatorException,ParticipationValidator.validate,participation)
        participation = Participation(1,"invalid",1)
        self.assertRaises(ParticipationValidatorException,ParticipationValidator.validate,participation)
        participation = Participation(1,1,"invalid")
        self.assertRaises(ParticipationValidatorException,ParticipationValidator.validate,participation)

if __name__ == '__main__':
    unittest.main()
