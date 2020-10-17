import os
import sys
import time

# https://qiita.com/reinhardhq/items/838df0bf09611f3c5872
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))
from modules.Data import Data
from modules.Config import Config
from modules.Logger import Logger
from modules.ProductManager import ProductManager

if __name__ == "__main__":
    config = Config.getConfig()
    logger = Logger.getLogger()
    
    manager = ProductManager()
    manager.init(config, logger)

    test1 = "Sample1"
    manager.set_product("Sample1", test1)

    test2 = manager.get_product("Sample1")
    print(test2)

    test3 = "Sample2"
    manager.set_element("Sample2", test3)

    test4 = manager.get_element("Sample2")
    print(test4)
