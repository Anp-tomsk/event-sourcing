from motorengine import Document, IntField, EmbeddedDocumentField
from actions.action_bus import bus


class Action(Document):
    __collection__ = "actions"

    action_type = IntField(required=True)
    payload = EmbeddedDocumentField(embedded_document_type=Document)


def create_action(action_type, payload):
    print("Payload {0}", payload)
    Action.objects.create(action_type=action_type, payload=payload,
                          callback=lambda action: bus.publish_message(action.to_son()))
