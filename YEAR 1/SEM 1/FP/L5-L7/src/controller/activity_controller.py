from domain.entities import Activity
from domain.validators import BookException
from _datetime import timedelta
import datetime
class ActivityControllerException(BookException):
    pass

class ActivityController(object):
    def __init__(self,activity_repository):
        """Initialize the activity repository."""
        self.__activity_repository = activity_repository

    def add(self,id:int,date:datetime.date,time:datetime.time,description:str):
        """Add a new person to the person repository.
        Args:
            id(uint): the id of the activity.
            date(datetime.date): the date on which the activity will take place.
            time(datetime.time): the time at which the activity will take place.
            description(str): the description of the activity.    
        Returns:
            None
        Raises:
            ActivityControllerException: if two activities overlap.
        """
        for activity in self.get_all():
            if activity.date == date and activity.time == time:
                raise ActivityControllerException("Activities must not overlap(not have the same starting date/time).")

        self.__activity_repository.save(Activity(id,date,time,description))

    def remove(self,id:int):
        """Remove an activity that matches the given id.
        Args:
            id(uint): the id of the activity to be removed.
        Returns None
        """
        self.__activity_repository.delete_by_id(id)
        
    def update(self,id:int,date:datetime.date,time:datetime.time,description:str):
        """Update an activity that macthes the given id.
        Args:
            id(uint): the id of the activity to be updated.
            date(datetime.date): the date on which the activity will take place.
            time(datetime.time): the time at which the activity will take place.
            description(str): the description of the activity.
        Returns:
            None
        """     
        self.__activity_repository.update(Activity(id,date,time,description))

    def get_all(self):
        """Return all of the activities as a dict list."""
        return self.__activity_repository.get_all()

    def find_by_id(self,id:int):
        """Find an activity that matches a given id.
        Args:
            id(uint): the id of the activity to be found.
        Returns:
            the activity matching the given id.
        """
        return self.__activity_repository.find_by_id(id)

    def find_by_date(self,date:datetime.date):
        """Find activities  matching a given date.
        Args:
            date(_datetime.date): the date on which the activities take
        Returns:
            the activities matching the given date.
        """
        return list(filter(lambda x: x.date == date,self.get_all()))

    def find_by_time(self,time:datetime.time):
        """Find activities matching a given time.
        Args:
            time(_datetime.time): the time in which the activities take place
        Returns:
            the activities matching the given time frame.
        """
        return list(filter(lambda x: x.time == time,self.get_all()))

    def find_by_description(self,description:str):
        """Find activities matching a given description(partial string matching).
        Args:
            description(str): the description of the activities to be found
        Returns:
            the activities matching the given description.
        """
        return list(filter(lambda x: description in x.description,self.get_all()))

    def find_by_day(self,day:int):
        """Find activities matching a given day.
        Args:
            day(uint): the day to find the activities for
        Returns:
            the activities taking place in the given day."""
        return list(filter(lambda x: x.date.day == day , self.get_all()))

    def __compute_week_date(self,week:int):
        """Compute the week date by a given week number.
        Args:
            week(uint): the week to compute the date for.
        Returns:
            the corresponding week date.
        """
        week_date = min(self.get_all(),key=lambda x: x.date).date+timedelta(days=7*(week))
        return week_date

    def find_by_week(self,week:int):
        """Find activities by a given week number.
        Args:
            week(uint): the week to find the activities for
        Returns:
            the activities taking place in the given week.
        """
        return list(filter(lambda x: x.date >= self.__compute_week_date(week-1) and x.date<=self.__compute_week_date(week),self.get_all()))