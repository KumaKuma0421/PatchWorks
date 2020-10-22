import time
import cv2
from templates.Interfaces import IProduct

class VideoCaptureProduct(IProduct):
    def __init__(self, id):
        super().__init__(id)
        self.capture = None
        self.isReady = False

    def start(self):
        self.logger.info("VideoCaptureProduct.start() IN")

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

        self.logger.info("VideoCaptureProduct.start() OUT")

    def process(self, value):
        now = time.perf_counter()
        value.add_processing_time(now)

        if self.isReady:
            _, image = self.capture.read()
            value.set_body(image)
        else:
            value.set_body(None)
        
        return value
