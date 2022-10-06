class Subscriber:
    
    _id = 0

    def get_id():
        Subscriber._id += 1
        return Subscriber._id

    def __new__(cls, *args, **kwargs):
        instance = super(Subscriber, cls).__new__(cls, *args, **kwargs)
        instance.id = Subscriber.get_id()
        return instance

    def _send(self, event):
        pass

    def send(self, event):
        event.sender = self.id
        self._send(event)

    def receive(self, event):
        pass
