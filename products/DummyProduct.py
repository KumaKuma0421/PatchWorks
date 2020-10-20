import time
import uuid
from templates.Interfaces import IProduct

class DummyProduct(IProduct):
    def __init__(self, id):
        super().__init__(id)

    def process(self, value):
        self.logger.info("DummyProduct[{0}].process()".format(self.id))
        
        for i, time_value in enumerate(value.get_processing_time()):
            self.logger.info("{0} Time[{1}]={2}".format(self.id, i, time_value))
        
        now = time.perf_counter()
        value.add_processing_time(now)
        
        if value.get_body() is None:
            value.set_body(list())
        else:
            for i, item in enumerate(value.get_body()):
                self.logger.info("{0} {1} body={2}".format(self.id, i, item))
        
        value.get_body().append(str(uuid.uuid4()))

        return value
