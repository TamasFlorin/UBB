from domain.validators import BookException
from domain.entities import Participation
from _functools import reduce
from domain.custom import filter
from domain.custom import sort
class ParticipationControllerException(BookException):
    pass

class ParticipationController(object):
    """Manage the participation of a person to an activity."""
    def __init__(self,participation_repository,person_controller,activity_controller):
        self.__participation_repository = participation_repository
        self.__person_controller = person_controller
        self.__activity_controller = activity_controller

    
    @staticmethod
    def read_entity(file_name):
        with open(file_name,'r') as f:
            line = f.read()
            line = line.split(" ")
            entity = Participation(int(line[0]),int(line[1]),int(line[2]))
            return entity

        return None

    @staticmethod
    def write_entity(file_name,entity):
        with open(file_name,'w') as f:
            line = str(entity.entity_id) + " " + str(entity.person_id) + " "+ str(entity.activity_id)
            f.write(line)

    def add(self,id,person_id,activity_id):
        """Add a participation to the repository.
        Args:
            id(uint): the id of the participation
            person_id(uint): the id of the person
            activity_id(uint): the id of the activity.
        Returns:
            None
        Raises:
            ParticipationControllerException: if the person_id does not exist in the person repository
                                              if the activity_id does not exist in the activity repository
        """
        if self.__person_controller.find_by_id(person_id) is None:
            raise ParticipationControllerException("No person with id {0} exists.".format(person_id))

        if self.__activity_controller.find_by_id(activity_id) is None:
            raise ParticipationControllerException("No activity with id {0} exists.".format(activity_id))

        self.__participation_repository.save(Participation(id,person_id,activity_id))

    def remove(self,id):
        """Remove a participation that has a given id.
        Args:
            id(uint): the id of the participation to be removed
        Returns:
            None
        """
        self.__participation_repository.delete_by_id(id)

    def update(self,id,person_id,activity_id):
        """Update a participation that has a given id.
        Args:
            id(uint): the id of the participation to be updated
            person_id(uint): the new person id
            activity_id(uint): the new activity id
        Returns:
            None
        """
        self.__participation_repository.update(Participation(id,person_id,activity_id))

    def get_all(self):
        """Returns a dict list with all the participation objects."""
        return self.__participation_repository.get_all()

    def find_by_id(self,participation_id):
        """Find a participation that matches a given id.
        Args:
            participation_id(uint): the id of the participation to be found.
        Returns:
            the participation that has the given id.
        """
        return self.__participation_repository.find_by_id(participation_id)

    def find_by_activity_id(self,activity_id):
        """Find a participation by the id of the activity."""
        return list(filter(lambda x: x.activity_id == activity_id,self.get_all()))

    def find_by_person_id(self,person_id):
        """Find a participation by the id of the person."""
        return list(filter(lambda x: x.person_id == person_id,self.get_all()))

    def find_by_activity_time(self,time):
        """Find a participation by the activity time."""
        return list(filter(lambda x: x.activity_id in [e.entity_id for e in self.__activity_controller.find_by_time(time)],self.get_all()))
        #return map(lambda x: self.__activity_controller.find_by_id(x.activity_id),list(filter(lambda x: x.activity_id in [e.entity_id for e in self.__activity_controller.find_by_time(time)],self.get_all())))

    def find_by_activity_date(self,date):
        """Find a participation by the activity date."""
        return list(filter(lambda x: x.activity_id in [e.entity_id for e in self.__activity_controller.find_by_date(date)],self.get_all()))
        #return map(lambda x: self.__activity_controller.find_by_id(x.activity_id),list(filter(lambda x: x.activity_id in [e.entity_id for e in self.__activity_controller.find_by_date(date)],self.get_all())))

    def find_by_activity_description(self,description):
        """Find a participation by the activity description."""
        return list(filter(lambda x: x.activity_id in [e.entity_id for e in self.__activity_controller.find_by_description(description)],self.get_all()))
        #return map(lambda x: self.__activity_controller.find_by_id(x.activity_id),list(filter(lambda x: x.activity_id in [e.entity_id for e in self.__activity_controller.find_by_description(description)],self.get_all())))

    def statistics_activity_by_day(self,day):
        """Create statistics for an activity that has a given day."""
        return list(filter(lambda x: x.activity_id in [e.entity_id for e in self.__activity_controller.find_by_day(day)],self.get_all()))
        #return map(lambda x: self.__activity_controller.find_by_id(x.activity_id),list(filter(lambda x: x.activity_id in [e.entity_id for e in self.__activity_controller.find_by_day(day)],self.get_all())))

    def statistics_activity_by_person(self,person_id):
        """Create statstics for participations that contain a given person."""
        return list(filter(lambda x: x.person_id ==person_id,self.get_all()))
        #return map(lambda x: self.__activity_controller.find_by_id(x.activity_id),list(filter(lambda x: x.person_id ==person_id,self.get_all())))

    def statistics_activity_by_week(self,week):
        """Create statistics for participations for a given week."""
        return list(filter(lambda x: x.activity_id in [e.entity_id for e in self.__activity_controller.find_by_week(week)],self.get_all()))

    def get_all_activities(self):
        """Return a dict list with all the activity objects."""
        return map(lambda x: self.__activity_controller.find_by_id(x.activity_id),list(filter(lambda x: x.activity_id in [e.entity_id for e in self.__activity_controller.get_all()],self.get_all())))

    def delete_by_activity_id(self,activity_id):
        """Delete a participation by the activity id."""
        for p in list(self.get_all())[:]:
            if p.activity_id==activity_id:
                self.__participation_repository.delete_by_id(p.entity_id)
    
    def delete_by_person_id(self,person_id):
        """Delete a participation by the person id."""
        for p in list(self.get_all())[:]:
            if p.person_id==person_id:
                self.__participation_repository.delete_by_id(p.entity_id)

    def statistics_sorted_busiest(self):
        """Sort the participation by the number of activities in each day."""
        #return list(set(map(lambda x: x.date,list(sorted(self.__activity_controller.get_all(),key = lambda z: len(self.__activity_controller.find_by_date(z.date)),reverse=True)))))
        return sorted(list(set(map(lambda x: x.date,list(sorted(self.__activity_controller.get_all(),key = lambda z: len(self.__activity_controller.find_by_date(z.date)),reverse=True))))),reverse=True)
    
    def statistics_sorted_persons(self):
        """Sort the participation by the number of persons attending to the activity."""
        return sorted(self.__person_controller.get_all(),key = lambda x: len(self.find_by_person_id(x.entity_id)),reverse=True)

    def delete_activity_and_participations(self,activity_id):
        self.delete_by_activity_id(activity_id)
        self.__activity_controller.remove(activity_id)

    def delete_person_and_participations(self,person_id):
        self.delete_by_person_id(person_id)
        self.__person_controller.remove(person_id)