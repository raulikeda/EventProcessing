import pytest
from src.event_processing.event import Event
from src.event_processing.subscriber import Subscriber


def test_subscriber_id_assignment():
    subscriber1 = Subscriber()
    subscriber2 = Subscriber()

    # Check that each subscriber gets a unique ID
    assert subscriber1.id != subscriber2.id


def test_subscriber_send_sets_sender_id():
    subscriber = Subscriber()
    event = Event(topic="test", partition="test", value="data")

    # Before sending, sender ID should be default
    assert event.sender == 0

    subscriber.send(event)

    # After sending, event's sender ID should be set to subscriber's ID
    assert event.sender == subscriber.id
