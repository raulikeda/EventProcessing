import pytest
from src.event_processing.event import Event
from src.event_processing.engine import Engine
from src.event_processing.subscriber import Subscriber


def test_event_subscription_and_dispatch():
    engine = Engine()
    subscriber = Subscriber()

    # Define a mock subscriber that records received events
    class MockSubscriber(Subscriber):
        def __init__(self):
            super().__init__()
            self.received_events = []

        def receive(self, event: Event):
            self.received_events.append(event)

    mock_subscriber = MockSubscriber()
    topic = "test_topic"

    # Subscribe the mock subscriber to the engine
    engine.subscribe(mock_subscriber, topic)

    # Create and send an event
    event = Event(topic=topic, partition=1, value="test_event")
    engine.inject(event)

    # Allow some time for the event to be processed
    # This is a simplistic approach; in real scenarios, consider using threading conditions or other synchronization methods.
    import time

    time.sleep(0.1)

    # Assert that the mock subscriber received the event
    assert len(mock_subscriber.received_events) == 1
    assert mock_subscriber.received_events[0].value == "test_event"
