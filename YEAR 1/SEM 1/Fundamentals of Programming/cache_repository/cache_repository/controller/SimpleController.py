from domain.SimpleEntity import SimpleEntity

class SimpleController(object):
    def __init__(self,simple_repository):
        self.__repository = simple_repository

    def add(self,entity_id,name,age):
        e = SimpleEntity(entity_id,name,age)

        self.__repository.save(e)

    def find_by_id(self,entity_id):
        return self.__repository.find_by_id(entity_id)

    def get_all(self):
        return self.__repository.get_all()


