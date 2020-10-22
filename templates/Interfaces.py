from templates.Observer import Observer, Subscriber


class IdentityObject:
    def __init__(self):
        self._id = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id


class IElement(Subscriber, Observer, IdentityObject):
    def __init__(self, id):
        super().__init__()
        self.id = id
        self._product = None

    def init(self):
        pass

    def start(self):
        pass

    def stop(self):
        pass

    def exit(self):
        pass

    @property
    def product(self):
        return self._product

    @product.setter
    def product(self, product):
        self._product = product


class IProduct(IdentityObject):
    def __init__(self, id):
        super().__init__()
        self.id = id
        self.config = None
        self.logger = None

    def init(self, config, logger):
        self.config = config
        self.logger = logger

    def start(self):
        pass

    def stop(self):
        pass

    def process(self, value):
        return value

    def command(self, context):
        pass

    def exit(self):
        pass


class IProductManager(object):
    def __init__(self):
        self.config = None
        self.logger = None

    def init(self, config, logger):
        self.config = config
        self.logger = logger

    def start(self):
        pass

    def stop(self):
        pass

    def command(self, context):
        pass

    def exit(self):
        pass
