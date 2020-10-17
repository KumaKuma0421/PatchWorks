import os
import sys
import time

# https://qiita.com/reinhardhq/items/838df0bf09611f3c5872
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))
from modules.Data import Data
from modules.Config import Config
from modules.Logger import Logger
from modules.DummyProduct import DummyProduct

if __name__ == "__main__":
    config = Config.getConfig()
    logger = Logger.getLogger()
    dummy = DummyProduct("dummy1")

    dummy.init(config, logger)
    dummy.start()
    data = Data(0)
    dummy.process(data)
    dummy.stop()
    dummy.exit()
