import os
import sys

# import common package in parent directroy
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))

from cloudAMQP_client import CloudAMQPClient

SCRAPE_NEWS_TASK_QUEUE_URL = "amqp://jxasfgzt:SVbuZ4h1nHcITLXebKg4QARp_SdolvSr@otter.rmq.cloudamqp.com/jxasfgzt"
SCRAPE_NEWS_TASK_QUEUE_NAME = "tap-news-scrape-news-task-queue"

DEDUPE_NEWS_TASK_QUEUE_URL = "amqp://xemwnewz:hLYOgqOnJS26oM24o-PP17mhXdbsWosb@otter.rmq.cloudamqp.com/xemwnewz"
DEDUPE_NEWS_TASK_QUEUE_NAME = "tap-news-dedupe-news-task-queue"

def clearQueue(queue_url, queue_name):
    queue_client = CloudAMQPClient(queue_url, queue_name)

    num_of_messages = 0

    while True:
        if queue_client is not None:
            msg = queue_client.getMessage()
            if msg is None:
                print("Clear %d message." % num_of_messages)
                return
            num_of_messages += 1

if __name__ == "__main__":
    clearQueue(SCRAPE_NEWS_TASK_QUEUE_URL, SCRAPE_NEWS_TASK_QUEUE_NAME)
    clearQueue(DEDUPE_NEWS_TASK_QUEUE_URL, DEDUPE_NEWS_TASK_QUEUE_NAME)