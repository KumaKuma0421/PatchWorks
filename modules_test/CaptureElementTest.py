import os
import sys
import time

# https://qiita.com/reinhardhq/items/838df0bf09611f3c5872
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

from templates.Observer import Observer
from modules.Data import Data
from modules.CaptureElement import CaptureElement
import cv2

WINDOW_TITLE="CaptureElementTest"

class TestObserver(Observer):
    def __init__(self):
        self.start = False
        self.previous_time = 0

    def ShowWindow(self):
        cv2.namedWindow(WINDOW_TITLE, cv2.WINDOW_AUTOSIZE | cv2.WINDOW_GUI_NORMAL)
        cv2.moveWindow(WINDOW_TITLE, 50, 50)

    def DestroyWindow(self):
        cv2.destroyWindow(WINDOW_TITLE)

    def update(self, value):
        if self.start == False:
            self.ShowWindow()
            self.start = True
        
        image = value.get_body()
        index = value.id
        process_time = value.get_processing_time()[0]
        interval = int((process_time - self.previous_time) * 1000)
        print("{0} {1} {2}".format(index, process_time, interval))
        cv2.imshow(WINDOW_TITLE, image)
        cv2.waitKey(1)
        self.previous_time = process_time
        


if __name__ == "__main__":
    capture=CaptureElement("test")
    observer=TestObserver()
    capture.attach(observer)

    capture.init(30)

    for n in range(3):
        capture.start()
        time.sleep(10)
        capture.stop()
        print("----------")
        time.sleep(3)
    
    #observer.DestroyWindow()
