from actions.device_actions import create_device
from actions.device_actions import assign_device
from actions.device_actions import unassign_device
from handlers.base_handler import BaseHandler


class DeviceHandler(BaseHandler):
    def post(self):
        self.prepare()
        device_model = self.json_args
        create_device(device_model.serial_number)


class AssignDeviceHandler(BaseHandler):
    def post(self):
        self.prepare()
        assign_model = self.json_args
        assign_device(assign_model.device_uid, assign_model.patient_uid)

    def delete(self):
        self.prepare()
        assign_model = self.json_args
        unassign_device(assign_model.device_uid, assign_model.patient_uid)