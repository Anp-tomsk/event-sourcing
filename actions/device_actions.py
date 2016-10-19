from motorengine import Document, UUIDField, IntField, StringField
from actions.action_types import ActionType
from actions.action import create_action
from enum import IntEnum
import uuid


class AssignmentInfo(IntEnum):
    assign = 1,
    unassign = 2


class AssignmentInfoAction(Document):
    __collection__ = "assignment_info"
    device_uid = UUIDField()
    patient_uid = UUIDField()
    assignment_type = IntField()


class CreateDeviceAction(Document):
    __collection__ = "create_device_actions"
    uid = UUIDField()
    serial_number = StringField()


def create_device(serial_number):
    print(serial_number)
    CreateDeviceAction.objects.create(uid=uuid.uuid1(), serial_number=serial_number,
                                      callback=lambda action: create_action(ActionType.create_device, action))


def assign_device(device_uid, patient_uid):
    AssignmentInfoAction.objects.create(device_uid=uuid.UUID(device_uid), patient_uid=uuid.UUID(patient_uid),
                                        assignment_type=AssignmentInfo.assign,
                                        callback=lambda action: create_action(ActionType.assignment_inf, action))


def unassign_device(device_uid, patient_uid):
    AssignmentInfoAction.objects.create(device_uid=uuid.UUID(device_uid), patient_uid=uuid.UUID(patient_uid),
                                        assignment_type=AssignmentInfo.unassign,
                                        callback=lambda action: create_action(ActionType.assignment_inf, action))