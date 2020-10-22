from modules.Logger import Logger
from modules.Config import Config
from modules.ClockElement import ClockElement
from modules.QueueElement import QueueElement
from modules.QueueElement import TerminateElement
from modules.SyncElement import SyncElement
from products.DummyProduct import DummyProduct
from products.VideoCaptureProduct import VideoCaptureProduct
from products.VideoPlayProduct import VideoPlayProduct
from products.VideoRecordProduct import VideoRecordProduct
from products.VideoViewProduct import VideoViewProduct
from products.ProductManager import ProductManager
from templates.Interfaces import IProduct, IElement

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
        product:IProduct = None

        if self._values["product"] == "DummyProduct":
            product = DummyProduct(self._values["id"])
        elif self._values["product"] == "VideoCaptureProduct":
            product = VideoCaptureProduct(self._values["id"])
        elif self._values["product"] == "VideoPlayProduct":
            product = VideoPlayProduct(self._values["id"])
        elif self._values["product"] == "VideoRecordProduct":
            product = VideoRecordProduct(self._values["id"])
        elif self._values["product"] == "VideoViewProduct":
            product = VideoViewProduct(self._values["id"])
        else:
            pass

        if product is not None:
            product.params = self._values
        
        return product
    
    def create(self):
        element = self.create_element()
        product = self.create_product()
        if product is not None:
            element.product = product

        return element, product

class FactoryMethod(object):
    def __init__(self, config, logger):
        self._config = config
        self._logger = logger

    def create(self):
        manager = ProductManager()

        for key, values in self._config.FlowDefine.Flow.items():
            self._logger.info(
                "flow[{0}] id={1} name={2} object={3} product={4} next={5}"
                .format(
                    key,
                    values["id"], values["name"], values["object"],
                    values["product"], values["next"]
                )
            )
            # --------------------
            element, product = Creator(values).create()
            manager.set_element(key, element)
            if product is not None:
                manager.set_product(key, product)
    
        for key, values in self._config.FlowDefine.Flow.items():
            if values["next"] != "None":
                if type(values["next"]) is str:
                    manager.get_element(key).attach(
                        manager.get_element(values["next"]))
                elif type(values["next"]) is list:
                    for distribute in values["next"]:
                        manager.get_element(key).attach(
                            manager.get_element(distribute))
                else:
                    raise ValueError(values["next"])

        return manager
