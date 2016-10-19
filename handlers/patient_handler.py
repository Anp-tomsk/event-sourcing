from actions.patient_actions import create_patient
from actions.patient_actions import edit_patient
from handlers.base_handler import BaseHandler


class PatientHandler(BaseHandler):
    def post(self):
        self.prepare()
        first_name, last_name = self.json_args
        create_patient(first_name, last_name)

    def put(self):
        self.prepare()
        edit_model = self.json_args
        edit_patient(edit_model.uid, edit_model.first_name, edit_model.last_name, edit_model.contact_info)
