from threading import Thread, Condition
from templates.Interfaces import IElement
from modules.Buffer import Buffer

class QueueElement(IElement):
    def __init__(self, id):
        super().__init__(id)
        self.init()

    def init(self):
        self.thread = None
        self.loop = False
        self.buffer = Buffer(self.id)

    def start(self):
        self.loop = True
        self.buffer.start()
        self.thread = Thread(target=self.run)
        self.thread.start()

    def stop(self):
        self.loop = False
        self.buffer.stop()
        self.thread.join()

    def run(self):
        while(self.loop):
            value = self.buffer.pop()
            if value is not None:
                if self.product is not None:
                    self.notify(self.product.process(value))
                else:
                    self.notify(value)

    def update(self, value):
        self.buffer.push(value)


class TerminateElement(QueueElement):
    def __init__(self, id):
        super().__init__(id)
        self.init()

    def run(self):
        while(self.loop):
            value = self.buffer.pop()
            del value

    def update(self, value):
        self.buffer.push(value)
