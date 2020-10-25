import os
import sys
import time
import math

# https://qiita.com/reinhardhq/items/838df0bf09611f3c5872
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

from templates.Observer import Observer
from modules.Data import Data
from modules.ClockElement import ClockElement


class TestObserver(Observer):
    def __init__(self):
        self.previous_time = 0

    def update(self, value):
        current_time = time.perf_counter()
        interval = math.floor((current_time - self.previous_time) * 1000)
        if type(value) is Data:
            print("{0}/{1}/{2}/{3}ms".format(
                value.id, value.get_command(),
                value.get_body(), interval))
            for item in value.get_processing_time():
                print("time is {0}".format(item))
        self.previous_time = current_time


if __name__ == "__main__":
    generator=ClockElement("test")
    observer=TestObserver()
    generator.attach(observer)

    generator.init(0.985)

    for n in range(3):
        generator.start()
        time.sleep(10)
        generator.stop()
        print("----------")
        time.sleep(3)
