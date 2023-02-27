import cv2
import matplotlib.pyplot as pylab
import numpy as np

lena=cv2.imread('images/black.png')
lena_double=lena+lena
b,g,r=cv2.split(lena)# 将图像分为b,g,r三部分
bgr=cv2.merge([b,g,r]) #按照bgr顺序合并图像
rgb=cv2.merge([r,g,b]) #按照rgb顺序合并图像
pylab.subplot(1,2,1)
pylab.imshow(bgr)
pylab.subplot(1,2,2)
pylab.imshow(rgb)
pylab.imshow(lena_double)
pylab.show()
cv2.waitKey(0)
