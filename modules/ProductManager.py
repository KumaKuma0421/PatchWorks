from templates.Interfaces import IProductManager

class ProductManager(IProductManager):
    def __init__(self):
        self._elements = dict()
        self._products = dict()

    def init(self, config, logger):
        self.config = config
        self.logger = logger

        for name, value in self._elements.items():
            print("init:" + name)
            if name == "clock":
                value.init(self.config.ClockGenerator.interval)
            else:
                value.init()
        
        for name, value in self._products.items():
            print("init:" + name)
            value.init(self.config, self.logger)
      

    def start(self):
        for name, value in self._elements.items():
            print("start:" + name)
            value.start()
        
        for name, value in self._products.items():
            print("start:" + name)
            value.start()

    def stop(self):
        for name, value in self._products.items():
            print("stop:" + name)
            value.stop()
        
        for name, value in self._elements.items():
            print("stop:" + name)
            value.stop()

    def command(self, context):
        pass

    def exit(self):
        for name, value in self._products.items():
            print("exit:" + name)
            value.exit()
        
        for name, value in self._elements.items():
            print("exit:" + name)
            value.exit()

    def get_product(self, id):
        return self._products[id]
    
    def set_product(self, id, value):
        self._products[id] = value

    def get_element(self, id):
        return self._elements[id]

    def set_element(self, id, value):
        self._elements[id] = value
