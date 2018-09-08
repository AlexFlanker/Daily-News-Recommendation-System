import os
import sys
import news_fetcher as fetcher
# import common package in parent directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))

from cloudAMQP_client import CloudAMQPClient

SCRAPE_NEWS_TASK_QUEUE_URL = "amqp://jxasfgzt:SVbuZ4h1nHcITLXebKg4QARp_SdolvSr@otter.rmq.cloudamqp.com/jxasfgzt"
SCRAPE_NEWS_TASK_QUEUE_NAME = "tap-news-scrape-news-task-queue"
scrape_news_queue_client  = CloudAMQPClient(SCRAPE_NEWS_TASK_QUEUE_URL, SCRAPE_NEWS_TASK_QUEUE_NAME)
TEST_MSG1 = ""
TEST_MSG2 = scrape_news_queue_client.get_message()
def test_basic():
    fetcher.handle_message(TEST_MSG1)
    fetcher.handle_message(TEST_MSG2)
    print('test_basic passed!')

if __name__ == "__main__":
    test_basic()
