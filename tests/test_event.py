from datetime import datetime
from src.event_processing.event import Event


def test_constructor():
    now = datetime.now
    event = Event('a', now, 'b', 1)

    assert event.topic == 'a'
    assert event.timestamp == now
    assert event.description == 'b'
    assert event.value == 1
