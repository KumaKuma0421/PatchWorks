from threading import Thread, Timer, Event
from templates.Observer import Subscriber
import time

class WatchDogTimer(Subscriber):
    def __init__(self):
        super().__init__()
        self.init()

    def init(self):
        self.interval = 0
        self.event = Event()
        self.loop = False
        self.thread = None
        self.previous_time = 0

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
            current_time = time.perf_counter()
            interval = current_time - self.previous_time
            offset = (interval - self.interval) * 0.1
            self.timer = Timer(self.interval - offset, self.trigger)
            #self.timer = Timer(self.interval, self.trigger)
            self.timer.start()
            self.event.wait()
            self.event.clear()
            self.previous_time = current_time

    def trigger(self):
        self.timer = None
        self.event.set()
        self.notify()