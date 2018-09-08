""" test unit of for cloudAMQP_client """
from cloudAMQP_client import CloudAMQPClient

TEST_CLOUDAMQP_URL = "amqp://fsdxexai:RmLazn-LRjEigo5J4NcH2kN9dB7nKMW6@otter.rmq.cloudamqp.com/fsdxexai"
TEST_QUEUE_NAME = "test"

def test_basic():
    """ test unit """
    client = CloudAMQPClient(TEST_CLOUDAMQP_URL, TEST_QUEUE_NAME)

    sent_msg = {'test' : 'test'}
    client.send_message(sent_msg)

    client.sleep(5)

    receive_msg = client.get_message()
    assert sent_msg == receive_msg

    print ('test_basic passed!')

if __name__ == "__main__":
    test_basic()
