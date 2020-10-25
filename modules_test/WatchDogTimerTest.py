import os
import sys
import threading
import unittest
import time

# https://qiita.com/reinhardhq/items/838df0bf09611f3c5872
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))
from modules.WatchDogTimer import WatchDogTimer
from templates.Observer import Observer


class TestObserver(Observer):
    def __init__(self):
        self.previous_time = 0
        self.counter = 1

    def update(self, value):
        current_time = time.perf_counter()
        interval = current_time - self.previous_time
        print("current:{0:9.5f} interval:{1:6.5f} counter:{2:3d} average:{3:6.5f}"
              .format(current_time, interval, self.counter, current_time / self.counter))
        self.previous_time = current_time
        self.counter += 1


class BufferTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_01(self):
        timer = WatchDogTimer()
        observer1 = TestObserver()
        #observer2 = TestObserver()
        timer.init()
        timer.attach(observer1)
        #timer.attach(observer2)
        timer.start(0.01)
        time.sleep(30)
        timer.stop()
        print("-----finished.")


if __name__ == "__main__":
    unittest.main()
