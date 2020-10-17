import os
import sys
import threading
import time

# https://qiita.com/reinhardhq/items/838df0bf09611f3c5872
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))
from modules.Data import Data
from modules.Logger import Logger
from modules.Config import Config
from modules.ClockElement import ClockElement
from modules.QueueElement import QueueElement, TerminateElement
from modules.SyncElement import SyncElement
from modules.DummyProduct import DummyProduct


class TerminateElement2(TerminateElement):
    def __init__(self, id):
        super().__init__(id)
        self.logger = Logger.getLogger()

    def update(self, value):
        self.logger.info("{0}/{1}/{2}".format(
            value.id, value.get_command(), value.get_body()))
        for item in value.get_processing_time():
            self.logger.info(" time is {0:3.3f}".format(item))
        super().update(value)

if __name__ == "__main__":
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
    queue5 = TerminateElement2("terminate")

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

    logger.info("stop Products")
    product1.stop()
    product2.stop()
    product3.stop()
    product4.stop()

    logger.info("stop Elements")
    queue0.stop()
    queue1.stop()
    queue2.stop()
    queue3.stop()
    queue4.stop()
    queue5.stop()

    logger.info(">>> ALL FINISHED <<<")
