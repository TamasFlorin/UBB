from domain.SimpleEntity import read_entity,write_entity
from repository.FileCacheRepository import FileCacheRepository
from ui.Console import Console
from controller.SimpleController import SimpleController

repository = FileCacheRepository(4,"simple.txt",read_entity,write_entity)
controller = SimpleController(repository)

console = Console(controller)
console.run()
