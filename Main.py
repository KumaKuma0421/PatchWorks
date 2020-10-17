#
# このプロジェクトのスタートアップスクリプト
#

import os
import sys
import threading
import time

from modules import DummyProduct
from modules import ClockElement, QueueElement, SyncElement, TerminateElement
from modules import Data
from modules import Logger
from modules import Config

def main():
    config = Config.getConfig()
    config.read()

    logger = Logger.getLogger()

    logger.info("Creating Elements")
    queue0 = ClockElement("clock")
    queue1 = QueueElement("queue1")
    #queue2 = QueueElement("sync1")
    queue2 = SyncElement("sync1")
    queue3 = QueueElement("queue2")
    queue4 = SyncElement("sync2")
    #queue4 = QueueElement("sync2")
    queue5 = TerminateElement("terminate")

    logger.info("Creating Products")
    product1 = DummyProduct("product1")
    product2 = DummyProduct("product2")
    product3 = DummyProduct("product3")
    product4 = DummyProduct("product4")

    logger.info("Attach Queues")
    queue0.attach(queue1)
    queue1.attach(queue2)
    queue2.attach(queue3)
    queue3.attach(queue4)
    queue4.attach(queue5)

    logger.info("Set Products")
    # queue0にはProductは不要
    queue1.product = product1
    queue2.product = product2
    queue3.product = product3
    queue4.product = product4
    # queue5にはProductは不要

    logger.info("Initialize Products")
    product1.init(config, logger)
    product2.init(config, logger)
    product3.init(config, logger)
    product4.init(config, logger)

    logger.info("Start Products")
    product1.start()
    product2.start()
    product3.start()
    product4.start()

    logger.info("Init Elements")
    queue0.init(config.ClockGenerator.interval)
    queue1.init()
    queue2.init()
    queue3.init()
    queue4.init()
    queue5.init()

    logger.info("Start Elements")
    queue0.start()
    queue1.start()
    queue2.start()
    queue3.start()
    queue4.start()
    queue5.start()

    logger.info("Now waiting 10 seconds")
    time.sleep(10)

    logger.info("Stop Products")
    product1.stop()
    product2.stop()
    product3.stop()
    product4.stop()

    logger.info("Stop Elements")
    queue0.stop()
    queue1.stop()
    queue2.stop()
    queue3.stop()
    queue4.stop()
    queue5.stop()

    logger.info(">>> ALL FINISHED <<<")

if __name__ == "__main__":
    main()