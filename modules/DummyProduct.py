import time
from templates.Interfaces import IProduct

class DummyProduct(IProduct):
    def __init__(self, id):
        super().__init__(id)

    def process(self, value):
        self.logger.info("DummyProduct[{0}].process()".format(self.id))
        #time.sleep(0.1)
        now = time.perf_counter()
        value.add_processing_time(now)
        return value
