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
        self.previous_time = 0
        self.show = False;

    def ShowWindow(self):
        cv2.namedWindow(WINDOW_TITLE, cv2.WINDOW_AUTOSIZE | cv2.WINDOW_GUI_NORMAL)
        cv2.moveWindow(WINDOW_TITLE, 50, 50)
        self.show = True;

    def DestroyWindow(self):
        cv2.destroyWindow(WINDOW_TITLE)
        self.show = False;

    def update(self, value):
        image = value.get_body()
        index = value.id
        process_time = value.get_processing_time()[0]
        interval = int((process_time - self.previous_time) * 1000)
        print("{0} {1} {2}".format(index, process_time, interval))
        if self.show:
            cv2.imshow(WINDOW_TITLE, image)
            cv2.waitKey(1)
        else:
            self.ShowWindow()
        self.previous_time = process_time
        


if __name__ == "__main__":
    capture=CaptureElement("test")
    observer=TestObserver()
    capture.attach(observer)

    capture.init(30)

    for n in range(3):
        capture.start()
        time.sleep(3)
        observer.ShowWindow()
        time.sleep(10)
        observer.DestroyWindow()
        capture.stop()
        print("----------")
        time.sleep(3)
    
    #observer.DestroyWindow()
