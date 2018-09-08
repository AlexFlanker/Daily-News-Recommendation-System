import os
import sys
import news_deduper as deduper
# import common package in parent directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from cloudAMQP_client import CloudAMQPClient

DEDUPE_NEWS_TASK_QUEUE_URL = "amqp://xemwnewz:hLYOgqOnJS26oM24o-PP17mhXdbsWosb@otter.rmq.cloudamqp.com/xemwnewz"
DEDUPE_NEWS_TASK_QUEUE_NAME = "tap-news-dedupe-news-task-queue"

cloudAMQP_client = CloudAMQPClient(DEDUPE_NEWS_TASK_QUEUE_URL, DEDUPE_NEWS_TASK_QUEUE_NAME)

TEST_MSG1 = ""
TEST_MSG2 = cloudAMQP_client.get_message()
def test_basic():
    deduper.handle_message(TEST_MSG1)
    deduper.handle_message(TEST_MSG2)
    print('test_basic passed!')

if __name__ == "__main__":
    test_basic()