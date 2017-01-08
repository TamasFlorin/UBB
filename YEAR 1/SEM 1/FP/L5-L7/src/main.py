
from repository.repository import Repository
from domain.validators import PersonValidator, ActivityValidator, ParticipationValidator
from controller.person_controller import PersonController
from controller.activity_controller import ActivityController
from controller.participation_controller import ParticipationController
from ui.console import Console
from repository.file_repository import FileRepository
from repository.pickle_repository import PickleRepository
from ui.Config import Config, StorageType

if __name__=="__main__":
    #try:
        config = Config("settings.properties")
        config.parse_config()

        print(config.storage_type)

        if(config.storage_type=="inmemory"):
            person_repository = Repository(PersonValidator)
            activity_repository = Repository(ActivityValidator)
            participation_repository = Repository(ParticipationValidator)
            person_controller = PersonController(person_repository)
            activity_controller = ActivityController(activity_repository)
            participation_controller=ParticipationController(participation_repository,person_controller,activity_controller)
            console = Console(person_controller,activity_controller,participation_controller)
            console.run()
            print("True")
        
        if(config.storage_type=="infile"):
            person_repository = FileRepository(config.person_repository,PersonController.read_entity,PersonController.write_entity,PersonValidator)
            activity_repository = FileRepository(config.activity_repository,ActivityController.read_entity,ActivityController.write_entity,ActivityValidator)
            participation_repository = FileRepository(config.participation_repository,ParticipationController.read_entity,ParticipationController.write_entity,ParticipationController)
            person_controller = PersonController(person_repository)
            activity_controller = ActivityController(activity_repository)
            participation_controller=ParticipationController(participation_repository,person_controller,activity_controller)
            console = Console(person_controller,activity_controller,participation_controller)
            console.run()
        
        if config.storage_type=="inpickledb":
            person_repository = PickleRepository(config.person_repository,PersonValidator)
            activity_repository = PickleRepository(config.activity_repository,ActivityValidator)
            participation_repository = PickleRepository(config.participation_repository,ParticipationValidator)
            person_controller = PersonController(person_repository)
            activity_controller = ActivityController(activity_repository)
            participation_controller=ParticipationController(participation_repository,person_controller,activity_controller)
            console = Console(person_controller,activity_controller,participation_controller)
            console.run()
   