class Observer(object):
    def update(self, value=None):
        pass


class Subscriber(object):
    def __init__(self):
        self._list = list()

    def attach(self, observer):
        self._list.append(observer)

    def detach(self, observer):
        self._list.remove(observer)

    def notify(self, value=None):
        for obj in self._list:
            obj.update(value)
