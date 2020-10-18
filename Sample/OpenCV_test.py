#
# see also https://news.mynavi.jp/article/zeropython-35/
#

import cv2

# カメラのキャプチャを開始 --- (*1)
cam = cv2.VideoCapture(0)

# カメラのfps、サイズを変更
print(cam.set(cv2.CAP_PROP_FPS, 30))
print(cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640))
print(cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480))

font = cv2.FONT_HERSHEY_SIMPLEX
counter = 0
line_counter = 0

WINDOW_TITLE_1 = "PUSH ENTER KEY"
WINDOW_TITLE_2 = "ANOTHER VIEW"
cv2.namedWindow(WINDOW_TITLE_1, cv2.WINDOW_AUTOSIZE | cv2.WINDOW_GUI_NORMAL)
cv2.namedWindow(WINDOW_TITLE_2, cv2.WINDOW_AUTOSIZE | cv2.WINDOW_GUI_NORMAL)
cv2.moveWindow(WINDOW_TITLE_1, 72, 64)
cv2.moveWindow(WINDOW_TITLE_2, 800, 64)

while True:
    # 画像を取得 --- (*2)
    _, img = cam.read()

    # ウィンドウに文字を表示
    text1 = "fps:{0:2.3}".format(cam.get(cv2.CAP_PROP_FPS))
    cv2.putText(img, text1, (4, 20), font, 0.7,
                (255, 255, 255), 0, cv2.LINE_AA)

    # ウィンドウに文字を表示
    text2 = "width:{0:4}".format(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
    cv2.putText(img, text2, (4, 42), font, 0.7,
                (255, 255, 255), 0, cv2.LINE_AA)

    # ウィンドウに文字を表示
    text3 = "height:{0:4}".format(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
    cv2.putText(img, text3, (4, 64), font, 0.7,
                (255, 255, 255), 0, cv2.LINE_AA)

    # ウィンドウに文字を表示
    text4 = "count:{0:4}".format(counter)
    cv2.putText(img, text4, (4, 86), font, 0.7,
                (255, 255, 255), 0, cv2.LINE_AA)

    # ウィンドウに直線を表示
    cv2.line(img, (0, 0), (line_counter, 0), (255, 0, 0), 5)
    line_counter += 1
    if line_counter >= 720:
        line_counter = 0

    # ウィンドウに矩形を表示
    cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)

    # ウィンドウに画像を表示 --- (*3)
    cv2.imshow(WINDOW_TITLE_1, img)
    counter += 1

    # 水平反転映像
    cv2.imshow(WINDOW_TITLE_2, cv2.flip(img, 1))

    # Enterキーが押されたら終了する
    if cv2.waitKey(30) == 13:
        break
# 後始末
cam.release()
cv2.destroyAllWindows()
