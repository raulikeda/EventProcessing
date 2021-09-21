from datetime import datetime
from src.event_processing.engine import Engine
from src.event_processing.subscriber import Subscriber
from src.event_processing.event import Event


def test_subscription():

    class Client(Subscriber):

        def receive(self, event):
            self.last = event

    client = Client()
    engine = Engine()

    # Case 1: Normal flow

    engine.subscribe(1, 'a', client.receive)
    engine.inject(Event('a', 't', 'd', 'v1'))

    assert client.last.value == 'v1'

    # Case 2: Second event

    engine.inject(Event('a', 't', 'd', 'v2'))
    assert client.last.value == 'v2'

    # Case 3: Another topic

    engine.inject(Event('b', 't', 'd', 'v3'))
    assert client.last.value == 'v2'

    # Case 4: Unsubscribe

    engine.unsubscribe(1, 'a')
    engine.inject(Event('a', 't', 'd', 'v4'))
    assert client.last.value == 'v2'

    # Case 5: Subscribe again

    engine.subscribe(1, 'c', client.receive)
    engine.inject(Event('a', 't', 'd', 'v5'))
    engine.inject(Event('c', 't', 'd', 'v6'))

    assert client.last.value == 'v6'
