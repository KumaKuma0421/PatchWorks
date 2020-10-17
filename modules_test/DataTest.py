import os
import sys
import unittest

# https://qiita.com/reinhardhq/items/838df0bf09611f3c5872
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))
from modules.Data import Data


class DataTest(unittest.TestCase):

    def setUp(self):
        print("setUp.")

    def tearDown(self):
        print("tearDown()")

    def test_01(self):
        expect0 = 0

        data = Data(expect0)

        self.assertEqual(expect0, data.id)

        expect1 = "sample_command"
        data.set_command(expect1)

        expect2 = "sample_body"
        data.set_body(expect2)

        print(data.get_command())
        self.assertEqual(expect1, data.get_command())
        print(data.get_body())
        self.assertEqual(expect2, data.get_body())


if __name__ == "__main__":
    unittest.main()
