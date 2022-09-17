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

    engine.subscribe(client.id, 'a', client.receive)
    engine.inject(Event('t', 'a', 'd', 'v1'))

    assert client.last.value == 'v1'

    # Case 2: Second event

    engine.inject(Event('t', 'a', 'd', 'v2'))
    assert client.last.value == 'v2'

    # Case 3: Another topic

    engine.inject(Event('t', 'b', 'd', 'v3'))
    assert client.last.value == 'v2'

    # Case 4: Unsubscribe

    engine.unsubscribe(1, 'a')
    engine.inject(Event('t', 'a', 'd', 'v4'))
    assert client.last.value == 'v2'

    # Case 5: Subscribe again

    engine.subscribe(1, 'c', client.receive)
    engine.inject(Event('t', 'a', 'd', 'v5'))
    engine.inject(Event('t', 'c', 'd', 'v6'))

    assert client.last.value == 'v6'
