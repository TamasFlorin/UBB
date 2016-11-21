
from repository.repository import Repository
from domain.validators import PersonValidator, ActivityValidator, ParticipationValidator
from controller.person_controller import PersonController
from controller.activity_controller import ActivityController
from controller.participation_controller import ParticipationController
from ui.console import Console

if __name__=="__main__":
    #try:
        person_repository = Repository(PersonValidator)
        person_controller = PersonController(person_repository)

        activity_repository = Repository(ActivityValidator)
        activity_controller = ActivityController(activity_repository)

        participation_repository = Repository(ParticipationValidator)
        participation_controller=ParticipationController(participation_repository,person_controller,activity_controller)

        console = Console(person_controller,activity_controller,participation_controller)

        console.run()

    #except Exception as ex:
       # print(ex)

