import time
import cv2
from templates.Interfaces import IProduct

WINDOW_TITLE = "Video View"

class VideoViewProduct(IProduct):
    def __init__(self, id):
        super().__init__(id)
    
    def start(self):
        cv2.namedWindow(WINDOW_TITLE, cv2.WINDOW_AUTOSIZE | cv2.WINDOW_GUI_NORMAL)
        cv2.moveWindow(WINDOW_TITLE, 72, 64)

    def process(self, value):
        self.logger.info("VideoViewProduct[{0}].process()".format(self.id))
        
        now = time.perf_counter()
        value.add_processing_time(now)

        image = value.get_body()
        if image is not None:
            cv2.imshow(WINDOW_TITLE, image)
        
        return value
    
    def stop(self):
        cv2.destroyAllWindows()
