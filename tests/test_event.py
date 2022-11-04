from datetime import datetime
from src.event_processing.event import Event


def test_constructor():
    now = datetime.now
    event = Event('a', 'b', 1, now)

    assert event.timestamp == now
    assert event.topic == 'a'
    assert event.partition == 'b'
    assert event.value == 1
