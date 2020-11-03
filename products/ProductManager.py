from templates.Interfaces import IProductManager


class ProductManager(IProductManager):
    def __init__(self):
        super().__init__()
        self._elements = dict()
        self._products = dict()

    def init(self, config, logger):
        self.config = config
        self.logger = logger
        self.logger.info("ProductManager.init() IN")

        # Elements initialized sequencial
        for name, value in self._elements.items():
            self.logger.info("initialize {0}-{1}".format(name, value.id))
            if value.id == "Clock":
                value.init(self.config.WatchDog.Interval)
            elif value.id == "Capture":
                value.init(self.config.WatchDog.Interval)
            else:
                value.init()

        # Products initialized sequencial 
        for name, value in self._products.items():
            self.logger.info("initialize {0}-{1}".format(name, value.id))
            value.init(self.config, self.logger)
        
        self.logger.info("ProductManager.init() OUT")

    def start(self):
        self.logger.info("ProductManager.start() IN")

        # Products start reversed sequencial
        for name, value in reversed(self._products.items()):
            self.logger.info("start {0}-{1}".format(name, value.id))
            value.start()

        # Elements start reversed sequencial
        for name, value in reversed(self._elements.items()):
            self.logger.info("start {0}-{1}".format(name, value.id))
            value.start()

        self.logger.info("ProductManager.start() OUT")

    def stop(self):
        self.logger.info("ProductManager.stop() IN")

        for name, value in self._products.items():
            self.logger.info("stop {0}-{1}".format(name, value.id))
            value.stop()

        for name, value in self._elements.items():
            self.logger.info("stop {0}-{1}".format(name, value.id))
            value.stop()

        self.logger.info("ProductManager.stop() OUT")

    def command(self, context):
        pass

    def exit(self):
        self.logger.info("ProductManager.exit() IN")

        for name, value in self._products.items():
            self.logger.info("stop {0}-{1}".format(name, value.id))
            value.exit()

        for name, value in self._elements.items():
            self.logger.info("stop {0}-{1}".format(name, value.id))
            value.exit()

        self.logger.info("ProductManager.exit() OUT")

    def get_product(self, id):
        return self._products[id]

    def set_product(self, id, value):
        self._products[id] = value

    def get_element(self, id):
        return self._elements[id]

    def set_element(self, id, value):
        self._elements[id] = value
