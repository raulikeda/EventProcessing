from src.event_processing.subscriber import Subscriber


def test_constructor():

    client = Subscriber()

    assert client.receive('a') == None
