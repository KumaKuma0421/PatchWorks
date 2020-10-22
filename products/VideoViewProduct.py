import threading
import time
import cv2
from templates.Interfaces import IdentityObject, IProduct
from modules.Buffer import Buffer


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
    def __init__(self, id, logger, params):
        self.id = id
        self._loop = False
        self.buffer = Buffer(id)
        self.logger = logger
        self.params = params
        self.title = params["title"]
        self.left = params["left"]
        self.top = params["top"]

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
                    self.title, cv2.WINDOW_AUTOSIZE | cv2.WINDOW_GUI_NORMAL)
                cv2.moveWindow(self.title, self.left, self.top)

            elif request.Command == request.command_stop:
                cv2.destroyWindow(self.title)

            elif request.Command == request.command_data:
                cv2.imshow(self.title, request.Body)
                cv2.waitKey(1)

            else:
                pass

        self.logger.info("VideoDisplaySubThread.process() OUT")


class VideoViewProduct(IProduct):
    def __init__(self, id):
        super().__init__(id)
        self.viewThread = None
        self.counter = 0

    def start(self):
        self.logger.info("VideoViewProduct.start() IN")

        self.counter = 0
        self.viewThread = VideoDisplaySubThread(
            self.id, self.logger, self.params)
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
            self.counter += 1
            request = Request()
            request.Command = request.command_data
            request.Body = self.add_info(image)
            self.viewThread.request(request)

        return value

    def add_info(self, image):
        start_row = 20
        offset_row = 22
        font = cv2.FONT_HERSHEY_SIMPLEX

        # 水平反転映像
        image = cv2.flip(image, 1)

        # ウィンドウに文字を表示
        text2 = "width:{0:4}".format(640) # TODO:暫定
        cv2.putText(image, text2, (4, start_row), font, 0.7,
                    (255, 255, 255), 0, cv2.LINE_AA)
        start_row += offset_row

        # ウィンドウに文字を表示
        text3 = "height:{0:4}".format(480) # TODO:暫定
        cv2.putText(image, text3, (4, start_row), font, 0.7,
                    (255, 255, 255), 0, cv2.LINE_AA)
        start_row += offset_row

        # ウィンドウに文字を表示
        text1 = "fps:{0:2.3}".format(30.0) # TODO:暫定
        cv2.putText(image, text1, (4, start_row), font, 0.7,
                    (255, 255, 255), 0, cv2.LINE_AA)
        start_row += offset_row

        # ウィンドウに文字を表示
        text4 = "count:{0:4}".format(self.counter)
        cv2.putText(image, text4, (4, start_row), font, 0.7,
                    (255, 255, 255), 0, cv2.LINE_AA)

        return image
