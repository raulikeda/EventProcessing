from datetime import datetime
from src.event_processing.event import Event


def test_constructor():
    now = datetime.now
    event = Event(now, 'a', 'b', 1)

    assert event.timestamp == now
    assert event.topic == 'a'
    assert event.partition == 'b'
    assert event.value == 1
