import time
import cv2
from templates.Interfaces import IProduct

class VideoCaptureProduct(IProduct):
    def __init__(self, id):
        super().__init__(id)
        self.capture = None
        self.isReady = False

    def start(self):
        self.capture = cv2.VideoCapture(0)

        if self.capture.set(cv2.CAP_PROP_FPS, 30) != True:
            self.logger.error("CV2 capture parameter set error. CAP_PROP_FPS")
            return
        
        if self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640) != True:
            self.logger.error("CV2 capture parameter set error. CAP_PROP_FRAME_WIDTH")
            return
        
        if self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) != True:
            self.logger.error("CV2 capture parameter set error. CAP_PROP_FRAME_HEIGHT")
            return
        
        self.isReady = True

    def process(self, value):
        self.logger.info("VideoCaptureProduct[{0}].process()".format(self.id))
        
        now = time.perf_counter()
        value.add_processing_time(now)

        if self.isReady:
            print("*" * 30)
            _, image = self.capture.read()
            value.set_body(image)
        else:
            print("-" * 30)
            value.set_body(None)
        
        return value
