#
# このプロジェクトのスタートアップスクリプト
#

import time
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
