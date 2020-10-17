from threading import Thread, Timer, Event
from templates.Observer import Subscriber

class WatchDogTimer(Subscriber):
    def __init__(self):
        super().__init__()
        self.init()

    def init(self):
        self.interval = 0
        self.event = Event()
        self.loop = False
        self.thread = None

    def start(self, interval):
        self.loop = True
        self.interval = interval
        self.thread = Thread(target=self.run)
        self.thread.start()

    def stop(self):
        self.loop = False
        self.thread.join()

    def run(self):
        while(self.loop):
            self.timer = Timer(self.interval, self.trigger)
            self.timer.start()
            self.event.wait()
            self.event.clear()

    def trigger(self):
        self.timer = None
        self.event.set()
        self.notify()