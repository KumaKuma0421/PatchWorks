import os
import sys
import time

# https://qiita.com/reinhardhq/items/838df0bf09611f3c5872
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

from templates.Observer import Observer
from modules.Data import Data
from modules.QueueElement import QueueElement

time_before = 0

class TestObserver(Observer):
    def update(self, value):
        if type(value) is Data:
            print("{0}/{1}/{2}".format(
                value.id, value.get_command(), value.get_body()))
            for item in value.get_processing_time():
                print("time is {0}".format(item))


if __name__ == "__main__":
    queue=QueueElement("test")
    observer=TestObserver()
    queue.attach(observer)

    queue.init()

    for n in range(3):
        queue.start()
        for i in range(10):
            now = time.perf_counter()
            data = Data(i)
            data.add_processing_time(now)
            data.set_command("frame")
            data.set_body("test {0} {1:5.3f}".format(i, now - time_before))
            queue.update(data)
            time.sleep(1)
        queue.stop()
        print("----------")
        time.sleep(3)
