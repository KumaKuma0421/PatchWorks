from templates.Interfaces import IElement


class SyncElement(IElement):
    def __init__(self, id):
        super().__init__(id)

    def update(self, value):
        if self.product is not None:
            self.notify(self.product.process(value))
        else:
            self.notify(value)
