from collections import deque
from threading import Condition
from templates.Interfaces import IdentityObject

class Buffer(IdentityObject):
    def __init__(self, id):
        self.id = id
        self.loop = False
        self.deque = deque()
        self.condition = Condition()

    def start(self):
        self.clear()
        self.loop = True

    def stop(self):
        self.loop = False
        self.push("stop")

    def push(self, value):
        with self.condition:
            self.deque.append(value)
            self.condition.notify_all()

    def pop(self):
        while self.loop:
            with self.condition:
                if self.size() > 0:
                    return self.deque.popleft()
                else:
                    self.condition.wait()
        return None

    def size(self):
        with self.condition:
            value = len(self.deque)
        return value

    def clear(self):
        with self.condition:
            self.deque.clear()


class Terminator(Buffer):
    def push(self, value):
        del value

    def update(self, value):
        self.push(value)
