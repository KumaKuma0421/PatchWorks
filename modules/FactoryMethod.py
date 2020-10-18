from modules.Logger import Logger
from modules.Config import Config
from modules.ClockElement import ClockElement
from modules.QueueElement import QueueElement
from modules.QueueElement import TerminateElement
from modules.SyncElement import SyncElement
from modules.ProductManager import ProductManager
from modules.DummyProduct import DummyProduct


class Creator(object):
    def __init__(self, values):
        self._values = values
    
    def create_element(self):
        if self._values["object"] == "ClockElement":
            return ClockElement(self._values["id"])
        elif self._values["object"] == "QueueElement":
            return QueueElement(self._values["id"])
        elif self._values["object"] == "TerminateElement":
            return TerminateElement(self._values["id"])
        else:
            return None

    def create_product(self):
        if self._values["product"] == "DummyProduct":
            return DummyProduct(self._values["id"])
        else:
            return None
    
    def create(self):
        element = self.create_element()
        product = self.create_product()
        element.set_product(product)

        return element, product

class FactoryMethod(object):
    def __init__(self, config, logger):
        self._config = config
        self._logger = logger

    def create(self):
        manager = ProductManager()

        for key, values in self._config.FlowDefine.Flow.items():
            self._logger.info(
                "flow[{0}] id={1} name={2} object={3} product={4} nect={5}"
                .format(
                    key,
                    values["id"], values["name"], values["object"],
                    values["product"], values["next"]
                )
            )
            # --------------------
            element, product = Creator(values).create()
            manager.set_element(values["name"], element)
            manager.set_product(values["name"], product)
            # --------------------
    


        clock.attach(queue0)
        queue0.attach(queue1)
        queue1.attach(queue2)
        queue2.attach(queue3)
        queue3.attach(terminate)

        return manager
