#
# see also https://news.mynavi.jp/article/zeropython-35/
#

import cv2

# カメラのキャプチャを開始 --- (*1)
cam = cv2.VideoCapture(0)

# カメラのfps、サイズを変更
print(cam.set(cv2.CAP_PROP_FPS, 30))
print(cam.set(cv2.CAP_PROP_FRAME_WIDTH, 720))
print(cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480))

font = cv2.FONT_HERSHEY_SIMPLEX
counter = 0

while True:
    # 画像を取得 --- (*2)
    _, img = cam.read()

    # ウィンドウに文字を表示
    text1 = "fps:{0:2.3}".format(cam.get(cv2.CAP_PROP_FPS))
    cv2.putText(img, text1, (4, 20), font, 0.7, (255,255,255), 0, cv2.LINE_AA)

    # ウィンドウに文字を表示
    text2 = "width:{0:4}".format(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
    cv2.putText(img, text2, (4, 42), font, 0.7, (255,255,255), 0, cv2.LINE_AA)

    # ウィンドウに文字を表示
    text3 = "height:{0:4}".format(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
    cv2.putText(img, text3, (4, 64), font, 0.7, (255,255,255), 0, cv2.LINE_AA)

    # ウィンドウに文字を表示
    text4 = "count:{0:4}".format(counter)
    cv2.putText(img, text4, (4, 86), font, 0.7, (255,255,255), 0, cv2.LINE_AA)
    
    # ウィンドウに画像を表示 --- (*3)
    cv2.imshow('PUSH ENTER KEY', img)
    cv2.moveWindow('PUSH ENTER KEY', 30, 30)
    counter += 1

    # Enterキーが押されたら終了する
    if cv2.waitKey(30) == 13:
        break
# 後始末
cam.release()
cv2.destroyAllWindows()
