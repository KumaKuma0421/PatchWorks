import os
import sys
import threading
import unittest
import time

# https://qiita.com/reinhardhq/items/838df0bf09611f3c5872
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))
from templates.Observer import Observer
from modules.WatchDogTimer import WatchDogTimer


class TestObserver(Observer):
    def update(self, value):
        print("timeup. {0}".format(time.perf_counter()))


class BufferTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_01(self):
        timer = WatchDogTimer()
        observer1 = TestObserver()
        observer2 = TestObserver()
        timer.init()
        timer.attach(observer1)
        timer.attach(observer2)
        timer.start(1)
        time.sleep(30)
        timer.stop()
        print("-----finished.")


if __name__ == "__main__":
    unittest.main()
