import time
import cv2
from templates.Interfaces import IProduct


class VideoPlayProduct(IProduct):
    def __init__(self, id):
        super().__init__(id)
        self.capture = None
        self.isReady = False

    def start(self):
        self.logger.info("VideoPlayProduct.start() IN")

        file_name = self.config.VideoPlay.VideoFile

        self.capture = cv2.VideoCapture(file_name)

        width = self.capture.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = self.capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
        fps = self.capture.get(cv2.CAP_PROP_FPS)
        self.logger.info(
            "FileName={0} Width={1} Height={2} FPS={3}".format(
                file_name, width, height, fps)
        )

        if (self.capture.isOpened()):
            self.isReady = True
            self.logger.info("VideoPlayProduct.start() OUT")
        else:
            self.logger.error(
                "VideoPlayProduct.start() Target File is not open.")

    def process(self, value):
        now = time.perf_counter()
        value.add_processing_time(now)

        if self.isReady:
            _, image = self.capture.read()
            value.set_body(image)
        else:
            value.set_body(None)

        return value
