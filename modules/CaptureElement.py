import time
import cv2
from threading import Thread
from templates.Interfaces import IElement
from modules.Data import Data


class CaptureElement(IElement):
    def __init__(self, id):
        super().__init__(id)
        self.init(0)
        self.capture = None
        self.thread = None
    
    def init(self, interval):        
        self.counter = 0
        self.time_before = 0
        self.interval = interval
        self.loop = False

    def start(self):
        self.counter = 0
        self.time_before = 0
        self.loop = True
        self.thread = Thread(target=self.run)
        self.thread.start()

    def stop(self):
        self.loop = False
        self.thread.join()

    def run(self):
        self.capture = cv2.VideoCapture(0)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.capture.set(cv2.CAP_PROP_FPS, self.interval)

        while self.loop:
            self.counter += 1
            now = time.perf_counter()
            data = Data(self.counter)
            data.add_processing_time(now)
            data.set_command("frame")
            _, image = self.capture.read()
            data.set_body(image)
            super().notify(data)
