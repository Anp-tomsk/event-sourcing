from motorengine import Document, StringField, UUIDField, EmbeddedDocumentField
from actions.action import create_action
from actions.action_types import ActionType
import uuid


class CreatePatientAction(Document):
    __collection__ = "create_patient_actions"
    uid = UUIDField()
    first_name = StringField()
    last_name = StringField()


class ContactInfo(Document):
    street = StringField()
    phone_number = StringField()
    email_address = StringField()


class EditPatientAction(Document):
    __collection__ = "edit_patient_actions"
    patientUid = UUIDField()
    new_first_name = StringField()
    new_last_name = StringField()
    contact_info = EmbeddedDocumentField(embedded_document_type=Document)


def edit_patient(uid, first_name, last_name, contact_info):
    street, phone_number, email_address = contact_info
    contact_doc = ContactInfo(street=street, email_address=email_address, phone_number=phone_number)
    EditPatientAction.objects.create(patientUid=uuid.UUID(uid), new_first_name=first_name, new_last_name=last_name,
                                     contact_info=contact_doc,
                                     callback=lambda action: create_action(ActionType.edit_patient, action))


def create_patient(first_name, last_name):
    CreatePatientAction.objects.create(uid=uuid.uuid1(), first_name=first_name, last_name=last_name,
                                       callback=lambda action: create_action(ActionType.create_patient, action))
