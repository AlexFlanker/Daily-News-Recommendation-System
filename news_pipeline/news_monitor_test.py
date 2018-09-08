import os
import sys
import news_monitor as monitor
from unittest.mock import MagicMock
# sys.path.append(os.path.join(os.path.dirname(__file__),'..', 'common'))
# import news_api_client
DEFAULT_SOURCES = ['cnn']
SORT_BY_TOP = 'top'
mock_news_api_client = MagicMock()
mock_news_api_client.return_value = ""
def test_basic():
    monitor.run(mock_news_api_client)
    print('test_basic passed!')

if __name__ == "__main__":
    test_basic()
