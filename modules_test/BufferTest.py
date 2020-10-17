import os
import sys
import threading
import unittest
import time

# https://qiita.com/reinhardhq/items/838df0bf09611f3c5872
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))
from modules.Buffer import Buffer, Terminator
from modules.Logger import Logger

class BufferTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_01(self):
        buf1 = Buffer("buf1")
        buf2 = Buffer("buf2")
        buf3 = Buffer("buf3")

        buf1.start()
        buf2.start()
        buf3.start()

        expect = "test_test_test"

        buf1.push(expect)
        self.assertEqual(1, buf1.size())

        value2 = buf1.pop()
        self.assertEqual(0, buf1.size())
        self.assertEqual(expect, value2)

        buf2.push(value2)
        self.assertEqual(1, buf2.size())

        value3 = buf2.pop()
        self.assertEqual(0, buf2.size())
        self.assertEqual(expect, value3)

        buf3.push(value3)
        self.assertEqual(1, buf3.size())

        actual = buf3.pop()
        self.assertEqual(0, buf3.size())
        self.assertEqual(expect, actual)
    
    def test_02(self):
        buf1 = Buffer("buf1")

        for i in range(1, 10):
            value = "TEST_{0}".format(i)
            buf1.push(value)
            self.assertEqual(i, buf1.size())
        
        buf1.clear()
        self.assertEqual(0, buf1.size())
    
    def work1(self):
        while(self.loop_work1):
            time.sleep(1)
            self.buffer.push("TEST {0}".format(time.time()))
            self.logger.info("work1 pushed")
    
    def work2(self):
        while(self.loop_work2):
            val = self.buffer.pop()
            self.logger.info("work2 poped({0})".format(val))

    def test_03(self):
        self.logger = Logger().getLogger()
        self.loop_work1 = True
        self.loop_work2 = True
        self.buffer = Buffer("TEST")
        self.buffer.start()
        self.logger.info("test_03 started")
        threading.Thread(target=self.work1).start()
        threading.Thread(target=self.work2).start()
        time.sleep(30)
        self.loop_work1 = False
        self.loop_work2 = False
        self.buffer.stop()
        self.logger.info("test_03 stoped")


if __name__ == "__main__":
    unittest.main()
