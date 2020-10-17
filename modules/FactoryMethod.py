from modules.Logger import Logger
from modules.Config import Config
from modules.ClockElement import ClockElement
from modules.QueueElement import QueueElement
from modules.QueueElement import TerminateElement
from modules.SyncElement import SyncElement
from modules.ProductManager import ProductManager
from modules.DummyProduct import DummyProduct


class FactoryMethod(object):
    def __init__(self):
        pass

    def create(self):
        manager = ProductManager()

        # --------------------
        clock = ClockElement("clock")
        manager.set_element("clock", clock)

        # --------------------
        queue0 = QueueElement("queue0")
        manager.set_element("queue0", queue0)

        product0 = DummyProduct("product0")
        manager.set_product("product0", product0)

        queue0.product = product0

        # --------------------
        queue1 = QueueElement("queue1")
        manager.set_element("queue1", queue1)

        product1 = DummyProduct("product1")
        manager.set_product("product1", product1)

        queue1.product = product1

        # --------------------
        queue2 = QueueElement("queue2")
        manager.set_element("queue2", queue2)

        product2 = DummyProduct("product2")
        manager.set_product("product2", product2)

        queue2.product = product2

        # --------------------
        queue3 = QueueElement("queue3")
        manager.set_element("queue3", queue3)

        product3 = DummyProduct("product3")
        manager.set_product("product3", product3)

        queue3.product = product3

        # --------------------
        terminate = TerminateElement("terminate")
        manager.set_element("terminate", terminate)

        clock.attach(queue0)
        queue0.attach(queue1)
        queue1.attach(queue2)
        queue2.attach(queue3)
        queue3.attach(terminate)
        
        return manager