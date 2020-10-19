import os
import sys
import time

# https://qiita.com/reinhardhq/items/838df0bf09611f3c5872
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))
from modules.Data import Data
from modules.Config import Config
from modules.Logger import Logger
from modules.FactoryMethod import FactoryMethod

if __name__ == "__main__":
    config = Config.getConfig()
    config.read()
    logger = Logger.getLogger()
    
    factory = FactoryMethod(config, logger)
    manager = factory.create()

    manager.init(config, logger)
    
    for i in range(3):
        manager.start()
        time.sleep(5)
        manager.stop()
        time.sleep(5)
    
    manager.exit()
