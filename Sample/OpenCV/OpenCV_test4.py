#
# see also https://algorithm.joho.info/programming/python/opencv-videocapture-mp4-movie-py/
#

import cv2

cap = cv2.VideoCapture(0)
fps = 30

# 録画する動画のフレームサイズ（webカメラと同じにする）
size = (640, 480)

# 出力する動画ファイルの設定
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#video = cv2.VideoWriter('output.avi', fourcc, fps, size)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter('output.mp4', fourcc, fps, size)

while (cap.isOpened()):
    ret, frame = cap.read()

    # 画面表示
    cv2.imshow('frame', frame)

    # 書き込み
    video.write(frame)

    # キー入力待機
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 終了処理
cap.release()
video.release()
cv2.destroyAllWindows()
