import numpy as np
import cv2 as cv


cap = cv.VideoCapture(0)

while True:
    # 一帧一帧捕捉
    ret, frame = cap.read()
    # 我们对帧的操作在这里
    gray = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])
    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(gray, lower_blue, upper_blue)
    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame, frame, mask=mask)
    # 显示返回的每帧

    cv.imshow('frame', res)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
# 当所有事完成，释放 VideoCapture 对象
cap.release()
cv.destroyAllWindows()
