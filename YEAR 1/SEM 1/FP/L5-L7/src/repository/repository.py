from domain.validators import BookException, ValidatorException
from domain.custom import Iterable

class RepositoryException(BookException):
    pass

class DuplicateIdException(RepositoryException):
    pass

class IdNotFoundException(RepositoryException):
    pass

class Repository(object):
    """General-use repository class to store data."""
  
    def __init__(self,validator_class):
        self.__validator_class=validator_class
        self.__entities = {}

    @property
    def _entities(self):
        return self.__entities

    def find_by_id(self,entity_id):
        """Find an entity by a given id.
        Args:
            entity_id(uint): the entity id to return.
        Returns:
            the entity that matches the given id or None if no entity with the given id exists.
        """
        if entity_id in self.__entities:
            return self.__entities[entity_id]

        return None

    def save(self,entity):
        """Save the given entity into the repository.
        Args:
            entity: the entity to be saved(the entity_id must not already exist).
        Returns:
            None
        Raises:
            DuplicateIdException: if the id already exists.
            ValidatorException: if the entity is not valid.
        """
        try:
            self.__validator_class.validate(entity)
        except ValidatorException as ve:
            raise RepositoryException(ve)

        if not self.find_by_id(entity.entity_id) is None:
            raise DuplicateIdException("Duplicate entity id {0}".format(entity.entity_id))

        self.__entities[entity.entity_id] = entity

    def update(self,entity):
        """Update the given entity.
        Args:
            entity: the entity to be updated(the entity_id must already exist).
        Returns:
            None
        Raises:
            IdNotFoundException: if the entity does not exist.
            ValidatorException: if the given entity is not valid.
        """

        try:
            self.__validator_class.validate(entity)
        except ValidatorException as ve:
            raise RepositoryException(ve)

        if self.find_by_id(entity.entity_id) is None:
            raise IdNotFoundException("Entity id {0} does not exist.".format(entity.entity_id))

        self.__entities[entity.entity_id] = entity

    def delete_by_id(self,entity_id):
        """Delete an entity by a given id.
        Args:
            entity_id(uint): the id of the entity to be deleted.
        Returns:
            None
        Raises:
            IdNotFoundException: if the entity does not exist.
        """
        if self.find_by_id(entity_id) is None:
            raise IdNotFoundException("Entity id {0} does not exist.".format(entity_id))

        del self.__entities[entity_id]

    def get_all(self):
        """Return a list containing all the entities.
        Args:
            None
        Returns:
            the list containing all the entities.
        """
        return self.__entities.values()