import pytest
from datetime import datetime
from src.event_processing.event import Event


def test_event_initialization_and_repr():
    timestamp = datetime.now()
    event = Event(
        topic="test_topic",
        partition="test_partition",
        value="test_value",
        timestamp=timestamp,
    )

    # Verify that all attributes are correctly assigned
    assert event.topic == "test_topic"
    assert event.partition == "test_partition"
    assert event.value == "test_value"
    assert event.timestamp == timestamp

    # Verify the string representation
    expected_repr = f"{timestamp} - test_topic/test_partition: test_value"
    assert repr(event) == expected_repr
