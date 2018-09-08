import logging
import os
import sys
from newspaper import Article

# import common package in parent directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))

from cloudAMQP_client import CloudAMQPClient

SCRAPE_NEWS_TASK_QUEUE_URL = "amqp://jxasfgzt:SVbuZ4h1nHcITLXebKg4QARp_SdolvSr@otter.rmq.cloudamqp.com/jxasfgzt"
SCRAPE_NEWS_TASK_QUEUE_NAME = "tap-news-scrape-news-task-queue"

DEDUPE_NEWS_TASK_QUEUE_URL = "amqp://xemwnewz:hLYOgqOnJS26oM24o-PP17mhXdbsWosb@otter.rmq.cloudamqp.com/xemwnewz"
DEDUPE_NEWS_TASK_QUEUE_NAME = "tap-news-dedupe-news-task-queue"

SLEEP_TIME_IN_SECONDS = 5

logger_format = '%(asctime)s - %(message)s'
logging.basicConfig(format=logger_format)
logger = logging.getLogger('news_fetcher')
logger.setLevel(logging.DEBUG)

scrape_news_queue_client  = CloudAMQPClient(SCRAPE_NEWS_TASK_QUEUE_URL, SCRAPE_NEWS_TASK_QUEUE_NAME)
dedupe_news_queue_client  = CloudAMQPClient(DEDUPE_NEWS_TASK_QUEUE_URL, DEDUPE_NEWS_TASK_QUEUE_NAME)

def handle_message(msg):
    if not isinstance(msg, dict):
        logger.warning('message is broken')
        return
    
    text = None

    article = Article(msg['url'])
    article.download()
    article.parse()

    msg['text'] = article.text
    dedupe_news_queue_client.send_message(msg)

def run():
    while True:
        if scrape_news_queue_client is not None:
            msg = scrape_news_queue_client.get_message()

            if msg is not None:
                try:
                    handle_message(msg)
                except Exception as e:
                    logger.warning(e)
                    pass
            scrape_news_queue_client.sleep(SLEEP_TIME_IN_SECONDS)

if __name__ == "__main__":
    run()

