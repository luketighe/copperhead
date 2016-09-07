import unittest
from unittest.mock import Mock, MagicMock

from copperhead.util.eventhook import EventHook


class TestEventHook(unittest.TestCase):

    def test_should_add_subscriber(self):

        # arrange
        event_hook = EventHook()
        subscriber_mock = Mock()
        subscriber_mock.method = MagicMock()

        # act
        event_hook += subscriber_mock

        # assert
        self.assertEquals(1, len(event_hook._EventHook__handlers))

    def test_should_add_subscriber_once(self):

        # arrange
        event_hook = EventHook()
        subscriber_mock = Mock()
        subscriber_mock.method = MagicMock()

        # act
        event_hook += subscriber_mock
        event_hook += subscriber_mock

        # assert
        self.assertEquals(1, len(event_hook._EventHook__handlers))

    def test_should_remove_subscriber(self):

        # arrange
        event_hook = EventHook()
        subscriber_mock = Mock()
        subscriber_mock.method = MagicMock()

        subscriber_mock2 = Mock()
        subscriber_mock2.method = MagicMock()

        # act
        event_hook += subscriber_mock
        event_hook += subscriber_mock2

        event_hook -= subscriber_mock2

        # assert
        self.assertEquals(1, len(event_hook._EventHook__handlers))
        self.assertEquals(subscriber_mock, event_hook._EventHook__handlers[0])

    def test_should_not_remove_unknown_subscriber(self):
        # arrange
        event_hook = EventHook()
        subscriber_mock = Mock()
        subscriber_mock.method = MagicMock()

        # act
        event_hook -= subscriber_mock

        # assert
        self.assertEquals(0, len(event_hook._EventHook__handlers))

    def test_should_fire_single(self):

        # arrange
        event_hook = EventHook()
        subscriber_mock = Mock()
        subscriber_mock.method = MagicMock()
        event_hook += subscriber_mock.method
        event_hook += subscriber_mock.method

        # act
        args = ("some", "args")
        kwargs = {"some": "kwargs"}
        event_hook.fire(*args, **kwargs)

        # assert
        self.assertEquals(1, subscriber_mock.method.call_count)

    def test_should_fire_multiple_for_different_subscribers(self):
        # arrange
        event_hook = EventHook()
        subscriber_mock = Mock()
        subscriber_mock.method = MagicMock()
        subscriber_mock.method2 = MagicMock()
        event_hook += subscriber_mock.method
        event_hook += subscriber_mock.method2

        # act
        args = ("some", "args")
        kwargs = {"some": "kwargs"}
        event_hook.fire(*args, **kwargs)

        # assert
        self.assertEquals(1, subscriber_mock.method.call_count)
        self.assertEquals(1, subscriber_mock.method2.call_count)
