from enum import Enum
from domain.validators import BookException

def undo_add_person_handler(person_controller,person):

    # we need to be able to redo the operation
    CallStack.add_redo_operation(RedoHandlers.ADD_PERSON_HANDLER,person_controller,person)
    
    person_controller.remove(person.entity_id)

def undo_delete_person_handler(person_controller,person,participation_controller,participations):

    # we need to be able to redo the operation
    CallStack.add_redo_operation(RedoHandlers.DELETE_PERSON_HANDLER,person_controller,person,participation_controller,participations)

    person_controller.add(person.entity_id,person.name,person.phone_number,person.address)

    # also add the participations for the person
    for participation in participations:
        participation_controller.add(participation.entity_id,participation.person_id,participation.activity_id)

def undo_update_person_handler(person_controller,person):
    CallStack.add_redo_operation(RedoHandlers.UPDATE_PERSON_HANDLER,person_controller,person)

    person_controller.update(person.entity_id,person.name,person.phone_number,person.address)

# ========== HANDLERS FOR ACTIVITY==============

def undo_add_activity_handler(activity_controller,activity):
    CallStack.add_redo_operation(RedoHandlers.ADD_ACTIVITY_HANDLER,activity_controller,activity)

    activity_controller.remove(activity.entity_id)

def undo_delete_activity_handler(activity_controller,activity,participation_controller,participations):
    CallStack.add_redo_operation(RedoHandlers.DELETE_ACTIVITY_HANDLER,activity_controller,activity,participation_controller,participations)
    
    activity_controller.add(activity.entity_id,activity.date,activity.time,activity.description)

    for participation in participations:
        participation_controller.add(participation.entity_id,participation.person_id,participation.activity_id)

def undo_update_activity_handler(activity_controller,activity):
    CallStack.add_redo_operation(RedoHandlers.UPDATE_ACTIVITY_HANDLER,activity_controller,activity)
    activity_controller.update(activity.entity_id,activity.date,activity.time,activity.description)

# ========= HANDLERS FOR PARTICIPATION =========
def undo_add_participation_handler(participation_controller,participation):
    CallStack.add_redo_operation(RedoHandlers.ADD_PARTICIPATION_HANDLER,participation_controller,participation)

    participation_controller.remove(participation.entity_id)

def undo_remove_participation_handler(participation_controller,participation):
    CallStack.add_redo_operation(RedoHandlers.DELETE_PARTICIPATION_HANDLER,participation_controller,participation)
    participation_controller.add(participation.entity_id,participation.person_id,participation.activity_id)

def undo_update_participation_handler(participation_controller,participation):
    CallStack.add_redo_operation(RedoHandlers.UPDATE_PARTICIPATION_HANDLER,participation_controller,participation)
    participation_controller.update(participation.entity_id,participation.person_id,participation.activity_id)


class UndoHandlers(Enum):
    ADD_PERSON_HANDLER = undo_add_person_handler
    DELETE_PERSON_HANDLER = undo_delete_person_handler
    UPDATE_PERSON_HANDLER = undo_update_person_handler

    ADD_ACTIVITY_HANDLER = undo_add_activity_handler
    DELETE_ACTIVITY_HANDLER = undo_delete_activity_handler
    UPDATE_ACTIVITY_HANDLER = undo_update_activity_handler

    ADD_PARTICIPATION_HANDLER = undo_add_participation_handler
    DELETE_PARTICIPATION_HANDLER = undo_remove_participation_handler
    UPDATE_PARTICIPATION_HANDLER = undo_update_activity_handler


def redo_add_person_handler(person_controller,person):
    person_controller.add(person.entity_id,person.name,person.phone_number,person.address)

    # we also need to be able to undo this operation
    CallStack.add_undo_operation(UndoHandlers.ADD_PERSON_HANDLER,person_controller,person)

def redo_delete_person_handler(person_controller,person,participation_controller,participations):
    CallStack.add_undo_operation(UndoHandlers.DELETE_PERSON_HANDLER,person_controller,person_controller.find_by_id(person.entity_id),participation_controller,participation_controller.find_by_person_id(person.entity_id))

    person_controller.remove(person.entity_id)
    participation_controller.delete_by_person_id(person.entity_id)

def redo_update_person_handler(person_controller,person):
    CallStack.add_undo_operation(UndoHandlers.UPDATE_PERSON_HANDLER,person_controller,person)
    person_controller.update(person.entity_id,person.name,person.phone_number,person.address)

# ======== REDO ACTIVITY HANDLERS ========
def redo_add_activity_handler(activity_controller,activity):
    activity_controller.add(activity.entity_id,activity.date,activity.time,activity.description)

    CallStack.add_undo_operation(UndoHandlers.ADD_ACTIVITY_HANDLER,activity_controller,activity)

def redo_delete_activity_handler(activity_controller,activity,participation_controller,participations):
    CallStack.add_undo_operation(UndoHandlers.DELETE_ACTIVITY_HANDLER,activity_controller,activity,participation_controller,participations)

    activity_controller.remove(activity.entity_id)
    participation_controller.delete_by_activity_id(activity.entity_id)

def redo_update_activity_handler(activity_controller,activity):
    CallStack.add_undo_operation(UndoHandlers.UPDATE_ACTIVITY_HANDLER,activity_controller,activity)
    activity_controller.update(activity.entity_id,activity.date,activity.time,activity.description)

# ======= REDO PARTICIPATION HANDLERS ======
def redo_add_participation_handler(participation_controller,participation):
    participation_controller.add(participation.entity,participation.person_id,participation.activity_id)
    CallStack.add_undo_operation(UndoHandlers.ADD_PARTICIPATION_HANDLER,participation_controller,participation)

def redo_delete_participation_handler(participation_controller,participation):
    CallStack.add_undo_operation(UndoHandlers.DELETE_PARTICIPATION_HANDLER,participation_controller,participation)

    participation_controller.remove(participation.entity_id)

def redo_update_participation_handler(participation_controller,participation):
    CallStack.add_undo_operation(UndoHandlers.UPDATE_PARTICIPATION_HANDLER,participation_controller,participation)
    participation_controller.update(participation.entity_id,participation.person_id,participation.activity_id)

class RedoHandlers(Enum):
    ADD_PERSON_HANDLER = redo_add_person_handler
    DELETE_PERSON_HANDLER = redo_delete_person_handler
    UPDATE_PERSON_HANDLER = redo_update_person_handler

    ADD_ACTIVITY_HANDLER = redo_add_activity_handler
    DELETE_ACTIVITY_HANDLER = redo_delete_activity_handler
    UPDATE_ACTIVITY_HANDLER = redo_update_activity_handler

    ADD_PARTICIPATION_HANDLER = redo_add_participation_handler
    DELETE_PARTICIPATION_HANDLER = redo_delete_participation_handler
    UPDATE_PARTICIPATION_HANDLER = redo_update_participation_handler

class Operation(object):
    def __init__(self,handler,*args):
        self.__handler = handler
        self.__args = args

    @property
    def handler(self):
        return self.__handler

    @property
    def args(self):
        return self.__args

class CallStackException(BookException):
    pass

class CallStack(object):
    __undo_calls = []
    __redo_calls = []

    __redo_index = 0

    @staticmethod
    def add_undo_operation(handler,*args):
        CallStack.__undo_calls.append(Operation(handler,*args))
    
    @staticmethod
    def add_redo_operation(handler,*args):
        CallStack.__redo_calls.append(Operation(handler,*args))

    @staticmethod 
    def undo():
        call = CallStack.__undo_calls.pop()
        call.handler(*call.args)

    def redo():
        if CallStack.__redo_index==len(CallStack.__redo_calls):
            CallStack.__redo_calls.clear()
            CallStack.__redo_index = 0

        if not CallStack.__redo_calls:
            raise CallStackException("Nothing to redo.")

        call = CallStack.__redo_calls[CallStack.__redo_index]
        call.handler(*call.args)

        CallStack.__redo_index+=1