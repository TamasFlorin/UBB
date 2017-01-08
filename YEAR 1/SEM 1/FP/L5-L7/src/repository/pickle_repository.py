import pickle
from repository.repository import Repository

class PickleRepositoryException(Exception):
    pass

class PickleRepository(Repository):
    def __init__(self,file_name,validator_class):
        super().__init__(validator_class)
        self.__file_name = file_name
        self.__validator_class = validator_class
        self.read_data()

    def write_data(self):
        try:
            with open(self.__file_name,'wb') as f:
                pickle.dump(list(self.get_all()),f)
        except IOError:
            raise PickleRepositoryException("Couldn't find file {0}.".format(self.__file_name))

    def read_data(self):
        try:
            with open(self.__file_name,'rb') as f:
                try:
                    entities = pickle.load(f)
                    for e in entities:
                        self.save(e)
                except EOFError:
                    pass
        except IOError:
            raise PickleRepositoryException("Couldn't find file {0}.".format(self.__file_name))

    def save(self,entity):
        super().save(entity)
        self.write_data()