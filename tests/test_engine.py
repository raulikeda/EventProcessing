from datetime import datetime
from src.event_processing.engine import Engine
from src.event_processing.subscriber import Subscriber
from src.event_processing.event import Event


def test_subscription():

    class Client(Subscriber):
        def __init__(self):
            self.last = Event('', '', '', '')

        def receive(self, event):
            self.last = event
            if event.topic == 'c':
                self.send(Event('a','d','v1'))

    client = Client()
    engine = Engine()

    # Case 1: Normal flow

    engine.subscribe(client, 'a')
    client.send(Event('a', 'd', 'v1', 't'))

    assert client.last.value != 'v1'

    # Case 2: Second event

    engine.inject(Event('a', 'd', 'v2'))
    assert client.last.value == 'v2'

    # Case 3: Another topic

    engine.inject(Event('b', 'd', 'v3', 't'))
    assert client.last.value == 'v2'

    # Case 4: Unsubscribe

    engine.unsubscribe(1, 'a')
    engine.inject(Event('a', 'd', 'v4', 't'))
    assert client.last.value == 'v2'

    # Case 5: Subscribe again

    engine.subscribe(client, 'c')
    engine.inject(Event('a', 'd', 'v5', 't'))
    engine.inject(Event('c', 'd', 'v6', 't'))

    assert client.last.value == 'v6'

test_subscription