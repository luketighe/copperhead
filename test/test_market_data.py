import unittest
from unittest.mock import *
from copperhead.src.feed import FeedBase


class TestMarketData(unittest.TestCase):

    def test_feed_fire_event(self):

        # arrange
        feed = FeedBase()
        subscriber_mock = Mock()
        subscriber_mock.method = MagicMock()
        feed.onBarUpdate += subscriber_mock.method

        # act
        feed.new_bar(1)

        # assert
        self.assertEquals(1, subscriber_mock.method.call_count)
