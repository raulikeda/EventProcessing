# Event Processing

Welcome to EventProcessing, a lightweight, Python-based event handling system designed for efficient and straightforward event management and processing. This system allows for decoupled components, making it easier to develop and maintain complex applications with event-driven architectures.

## Features
* Simple API: Easy to use for subscribing to events, publishing events, and handling them.
* Decoupled Design: Promotes loose coupling between components for better modularity.
* Efficient Event Handling: Queue-based event processing ensuring order and reliability.

## Prerequisites
* Python 3.6+

## Installation
```sh
pip install event_processing
```

## Usage
Quick start guide and examples on how to subscribe to events, publish them, and handle them in your application.

### Creating an Engine
```python
# Create an engine for event handling
engine = Engine()
```

### Subscribing to an Event

```python
# Create a subscriber and subscribe to a topic
subscriber = Subscriber()
engine.subscribe(subscriber, "topic_name")
```

### Publishing an Event

```python
# Publish an event to a topic
event = Event(topic="topic_name", partition=1, value="Hello, World!")
engine.inject(event)
# Or with the subscriber itself
subscriber.send(event)
```

### Handling an Event
Implement the receive method in your Subscriber class.

```python
def receive(self, event: Event):
    print(f"Received event: {event.value}")
```

## Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

## License
Distributed under the MIT License. See LICENSE for more information.

## Contact
Project Link: https://github.com/raulikeda/EventProcessing
