import cv as cv
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

cap = cv.VideoCapture(0)

while 1:
    _, img = cap.read()
    edges = cv.Canny(img, 120, 200)
    imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(imgray, 127, 255, 0)
    contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cnt = contours[0]
    epsilon = 0.1 * cv.arcLength(cnt, True)
    approx = cv.approxPolyDP(cnt, epsilon, True)
    hull = cv.convexHull(cnt)
    k = cv.isContourConvex(cnt)






    # Convert BGR to HSV
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    kernel = np.ones((5, 5), np.float32) / 25
    gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)
    laplacian = cv.Laplacian(img,cv.CV_64F)
    sobelx = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=5)
    sobely = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=5)
    cv.imshow('sobelx', edges)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()

