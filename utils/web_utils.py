from utils.camel_to_snake import to_snake
from collections import namedtuple
import json


def decode_body(body):
    data = body.decode('ascii')
    return json.loads(data, object_hook=lambda d: namedtuple('X', map(to_snake, d.keys()))(*d.values()))
