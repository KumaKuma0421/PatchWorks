import time
from templates.Interfaces import IElement
from modules.Data import Data
from modules.WatchDogTimer import WatchDogTimer


class ClockElement(IElement):
    def __init__(self, id):
        super().__init__(id)
        self.init(0)
    
    def init(self, interval):
        self.timer = WatchDogTimer()
        self.timer.attach(self)
        self.interval = interval
        self.counter = 0
        self.time_before = 0

    def start(self):
        self.counter = 0
        self.time_before = 0
        self.timer.start(self.interval)

    def stop(self):
        self.timer.stop()

    def update(self, value):
        now = time.perf_counter()
        data = Data(self.counter)
        data.add_processing_time(now)
        data.set_command("frame")
        data.set_body(list())
        data.get_body().append("test {0} {1:3.3f}".format(self.counter, now - self.time_before))
        super().notify(data)
        self.counter += 1
