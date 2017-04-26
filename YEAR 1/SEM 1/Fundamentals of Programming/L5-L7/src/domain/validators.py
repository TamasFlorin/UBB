import datetime

class BookException(Exception):
    pass

class ValidatorException(BookException):
    pass

class PersonValidatorException(ValidatorException):
    pass

class ActivityValidatorException(ValidatorException):
    pass

class ParticipationValidatorException(ValidatorException):
    pass

class PersonValidator(object):
    """Validate the person object."""
    @staticmethod
    def __is_valid_phone_number(phone_number):
        """Check if a given phone number is valid.
        Args:
            phone_number(str): the phone number to check.
        Returns:
            True if the phone number is valid,False otherwise.
        """
        if len(phone_number)!=10:
            return False

        for c in phone_number:
            if c.isdigit()==False:
                return False

        return True

    @staticmethod
    def validate(person):
        """Validate a person object by checking the type of it's attributes.
        Args:
            person(Person): the person object to be validated.
        Raises:
            PersonValidatorException: if the type of the entity_id is not int
                                      if the type of the name is not str
                                      if the type of the phone number is not str
                                      if the phone number format is invalid
                                      if the type of the address is not str
        """
        if not type(person.entity_id) is int:
            raise PersonValidatorException("Person id must be an integer.")

        if not type(person.name) is str:
            raise PersonValidatorException("Person name must be a string.")

        if not type(person.phone_number) is str:
            raise PersonValidatorException("Person phone number must be a string.")

        if not PersonValidator.__is_valid_phone_number(person.phone_number):
            raise PersonValidatorException("Person phone number can only contain digits.")

        if not type(person.address) is str:
            raise PersonValidatorException("Person address must be a string.")

class ActivityValidator(object):
    """Validate the activity object."""
    @staticmethod
    def validate(activity):
        """Validate an activity object by checking the type of it's attributes.
        Args:
            activity(Activity): the activity object to be validated.
        Raises:
            ActivityValidatorException: if entity_id is not of type int
                                        if date is not of type datetime.date
                                        if time is not of type datetime.time
                                        if description if not of type str
        """

        if not type(activity.entity_id) is int:
            raise ActivityValidatorException("Activity id must be an integer.")

        if not type(activity.date) is datetime.date:
            raise ActivityValidatorException("Activity date must be of type datetime.date.")

        if not type(activity.time) is datetime.time:
            raise ActivityValidatorException("Activity time must be of type datetime.time.")

        if not type(activity.description) is str:
            raise ActivityValidatorException("Activity description must be a string.")

class ParticipationValidator(object):
    """Validate the participation object."""
    @staticmethod
    def validate(participation):
        """Validate a participation object by checking the type of it's attributes.
        Args:
            participation(Participation): the participation object to be validated.
        Raises:
            ParticipationValidatorException: if the type of the entity_id is not int
                                             if the type of the person_id is not int
                                             if the type of the activity_id is not int
        """
        if not type(participation.entity_id) is int:
            raise ParticipationValidatorException("Participation id must be an integer.")

        if not type(participation.person_id) is int:
            raise ParticipationValidatorException("Participation person id must be an integer.")

        if not type(participation.activity_id) is int:
            raise ParticipationValidatorException("Participation activity id must be an integer.")



