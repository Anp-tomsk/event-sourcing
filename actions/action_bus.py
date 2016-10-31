import pika


class ActionBus:
    def __init__(self, amqp_url):
        self._channel = None
        self._connected = False
        self._url = amqp_url

    def reconnect(self):
        connection = pika.BlockingConnection(pika.URLParameters(self._url))

        self._channel = connection.channel()
        self._channel.queue_declare(queue='ES')
        self._connected = True

    def publish_message(self, message):
        print(message)
        if not self._connected:
            self.reconnect()

        try:
            self._channel.basic_publish(exchange='amq.direct', routing_key='actions', body=message.__str__())
        except:
            self._connected = False
            raise

bus = ActionBus('')
