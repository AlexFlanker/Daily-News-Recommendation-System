""" test for get one news """
import sys
import os
import operations
sys.path.append(os.path.join(os.path.dirname(__file__),'..', 'common'))
from cloudAMQP_client import CloudAMQPClient

LOG_CLICKS_TASK_QUEUE_URL = "amqp://pdliekxt:8mgB93yc2_88oIpNbXSRDxpAXFvyy7wv@otter.rmq.cloudamqp.com/pdliekxt"
LOG_CLICKS_TASK_QUEUE_NAME = "log_clicks"

cloudAMQP_client = CloudAMQPClient(LOG_CLICKS_TASK_QUEUE_URL, LOG_CLICKS_TASK_QUEUE_NAME)

def test_getOneNewsBasic():
    """ test unit """
    news = operations.getOneNews()
    print (news)
    assert news is not None
    print ('test_get_one_news_basic passed!')

def test_getNewsSummariesForUserBasic():
    news = operations.getNewsSummariesForUser('test_user', 1)
    print (news)
    assert len(news) > 0
    print('test_get_news_summaries_for_user_basic passed!')

def test_getNewsSummariesForUserInvalidPage_num():
    news = operations.getNewsSummariesForUser('test_user', -1)
    assert len(news) == 0
    print('test_get_news_summaries_for_user_invalid_page_num passed!')

def test_getNewsSummariesForUserLargePage_num():
    news = operations.getNewsSummariesForUser('test_user', 1000)
    assert len(news) == 0
    print('test_get_news_summaries_for_user_large_page_num passed!')

def test_getNewsSummariesForUserPagination():
    news_page_1 = operations.getNewsSummariesForUser('test_user', 1)
    news_page_2 = operations.getNewsSummariesForUser('test_user', 2)

    assert len(news_page_1) > 0
    assert len(news_page_2) > 0

    digest_page_1_set = set([news['digest'] for news in news_page_1])
    digest_page_2_set = set([news['digest'] for news in news_page_2])

    assert len(digest_page_1_set.intersection(digest_page_2_set)) == 0

    print('test_get_news_summaries_for_use_pagination passed!')

def test_logNewsClickForUser():
    operations.logNewsClickForUser('test_user', 'test_news')
    msg = cloudAMQP_client.get_message()
    assert msg['userId'] == 'test_user'
    assert msg['newsId'] == 'test_news'

    print('test_logNewsClickForUser passed!')


if __name__ == "__main__":
    test_getOneNewsBasic()
    test_getNewsSummariesForUserBasic()
    test_getNewsSummariesForUserInvalidPage_num()
    test_getNewsSummariesForUserLargePage_num()
    test_getNewsSummariesForUserPagination()
    # test_logNewsClickForUser()
