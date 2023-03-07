import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while 1:
    # Take each frame
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    kernel = np.ones((5, 5), np.float32) / 25
    gradient = cv.morphologyEx(frame, cv.MORPH_GRADIENT, kernel)
    # define range of blue color in HSV
    lower_blue = np.array([26, 43, 46])
    upper_blue = np.array([34, 255, 255])
    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_blue, upper_blue)
    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame, frame, mask=mask)
    ret1, th1 = cv.threshold(frame, 127, 255, cv.THRESH_BINARY)
    kernel = np.ones((5, 5), np.float32) / 25
    dst = cv.filter2D(frame, -1, kernel)
    # ret2, th2 = cv.threshold(frame, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
    # 经过高斯滤波的 Otsu 阈值
    # blur = cv.GaussianBlur(res, (5, 5), 0)
    # ret3, th3 = cv.threshold(blur, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

    cv.imshow('frame', gradient)
    # cv.imshow('mask', mask)
    # cv.imshow('res', th1)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()
