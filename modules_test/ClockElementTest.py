import os
import sys
import time

# https://qiita.com/reinhardhq/items/838df0bf09611f3c5872
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

from templates.Observer import Observer
from modules.Data import Data
from modules.ClockElement import ClockElement


class TestObserver(Observer):
    def update(self, value):
        if type(value) is Data:
            print("{0}/{1}/{2}".format(
                value.id, value.get_command(), value.get_body()))
            for item in value.get_processing_time():
                print("time is {0}".format(item))


if __name__ == "__main__":
    generator=ClockElement("test")
    observer=TestObserver()
    generator.attach(observer)

    generator.init(0.33)

    for n in range(3):
        generator.start()
        time.sleep(10)
        generator.stop()
        print("----------")
        time.sleep(3)
