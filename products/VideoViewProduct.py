import threading
import time
import cv2
from templates.Interfaces import IdentityObject, IProduct
from modules.Buffer import Buffer

WINDOW_TITLE = "Video View"


class Request(object):
    command_start = 0
    command_stop = 1
    command_data = 2

    def __init__(self):
        self._command = None
        self._body = None

    @property
    def Command(self):
        return self._command

    @Command.setter
    def Command(self, value):
        self._command = value

    @property
    def Body(self):
        return self._body

    @Body.setter
    def Body(self, value):
        self._body = value


class VideoDisplaySubThread(IdentityObject):
    def __init__(self, id, logger):
        self.id = id
        self._loop = False
        self.buffer = Buffer(id)
        self.logger = logger

    def start(self):
        self.logger.info("VideoDisplaySubThread.start() IN")
        self._loop = True
        self.buffer.start()
        self._thread = threading.Thread(target=self.process)
        self._thread.start()
        self.logger.info("VideoDisplaySubThread.start() OUT")

    def stop(self):
        self.logger.info("VideoDisplaySubThread.stop() IN")
        self._loop = False
        self.buffer.stop()
        self._thread.join()
        self.logger.info("VideoDisplaySubThread.stop() OUT")

    def request(self, request):
        self.buffer.push(request)

    def process(self):
        self.logger.info("VideoDisplaySubThread.process() IN")
        while self._loop:
            request = self.buffer.pop()
            if request.Command == request.command_start:
                cv2.namedWindow(
                    WINDOW_TITLE, cv2.WINDOW_AUTOSIZE | cv2.WINDOW_GUI_NORMAL)
                cv2.moveWindow(WINDOW_TITLE, 72, 64)

            elif request.Command == request.command_stop:
                cv2.destroyWindow(WINDOW_TITLE)

            elif request.Command == request.command_data:
                cv2.imshow(WINDOW_TITLE, request.Body)
                cv2.waitKey(1)

            else:
                pass

        self.logger.info("VideoDisplaySubThread.process() OUT")


class VideoViewProduct(IProduct):
    def __init__(self, id):
        super().__init__(id)
        self.viewThread = None

    def start(self):
        self.logger.info("VideoViewProduct.start() IN")

        self.viewThread = VideoDisplaySubThread(self.id, self.logger)
        self.viewThread.start()
        request = Request()
        request.Command = request.command_start
        self.viewThread.request(request)

        self.logger.info("VideoViewProduct.start() OUT")

    def stop(self):
        self.logger.info("VideoViewProduct.stop() IN")

        request = Request()
        request.Command = request.command_stop
        self.viewThread.request(request)
        self.viewThread.stop()

        self.logger.info("VideoViewProduct.stop() OUT")

    def process(self, value):
        now = time.perf_counter()
        value.add_processing_time(now)

        image = value.get_body()
        if image is not None:
            request = Request()
            request.Command = request.command_data
            request.Body = image
            self.viewThread.request(request)

        return value
