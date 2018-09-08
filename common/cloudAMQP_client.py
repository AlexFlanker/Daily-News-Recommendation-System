""" cloudAMQP """
import json
import logging
import pika

LOGGER_FORMAT = '%(asctime)s - %(message)s'
logging.basicConfig(format=LOGGER_FORMAT)
LOGGER = logging.getLogger('cloud_amqp_client')
LOGGER.setLevel(logging.DEBUG)

class CloudAMQPClient:
    """ class params define"""
    def __init__(self, cloud_amqp_url, queue_name):
        self.cloud_amqp_url = cloud_amqp_url
        self.queue_name = queue_name
        self.params = pika.URLParameters(cloud_amqp_url)
        self.params.socket_timeout = 3
        self.connection = pika.BlockingConnection(self.params)
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=queue_name)


    # Send a message.
    def send_message(self, message):
        """ Send Message Function"""
        self.channel.basic_publish(exchange='', 
                                   routing_key=self.queue_name, 
                                   body=json.dumps(message))
        LOGGER.debug("[x] send message to %s:%s", self.queue_name, message)

    # Get a message. If no message, return None.
    def get_message(self):
        """ Get Message Function"""
        method_frame, header_frame, body = self.channel.basic_get(self.queue_name)
        if method_frame:
            LOGGER.debug("[x] Received message from %s:%s", self.queue_name, body)
            self.channel.basic_ack(method_frame.delivery_tag)
            return json.loads(body.decode('utf-8'))
        else:
            LOGGER.debug("No message returned")
            return None


    # BlockingConnection.sleep is a safer way to sleep than time.sleep(). This
    # will repond to server's heartbeat.
    def sleep(self, seconds):
        """ Sleep """
        self.connection.sleep(seconds)
