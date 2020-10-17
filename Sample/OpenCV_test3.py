#
# see also https://algorithm.joho.info/programming/python/opencv-videocapture-mp4-movie-py/
#

import cv2
import numpy as np

filepath = r"C:\Users\User01\Sources\GitHub\PatchWorks\Sample"
filename = r"mov_hts-samp005.mp4"

# 動画の読み込み
cap = cv2.VideoCapture(filepath + "\\" + filename)

# 動画のプロパティを取得
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = cap.get(cv2.CAP_PROP_FPS)
frame_num = cap.get(cv2.CAP_PROP_FRAME_COUNT)
play_time = frame_num / fps

# 動画のプロパティを表示
print("WIDTH:", width)
print("HEIGHT:", height)
print("FPS:", fps)
print("FRAME NUM:", frame_num)
print("Play TIME[sec]:", play_time)

# 動画終了まで繰り返し
while(cap.isOpened()):
    # フレームを取得
    ret, frame = cap.read()

    # フレームを表示
    cv2.imshow("Frame", frame)

    # qキーが押されたら途中終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
