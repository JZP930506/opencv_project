import cv2
import matplotlib.pyplot as pylab

class Spliter:
    @staticmethod
    def ShowSpliterPicture():
        lena = cv2.imread('../images/cat.jpg')
        pylab.subplot(1, 4, 1)
        pylab.imshow(lena)
        lena_double = lena+lena
        b, g, r = cv2.split(lena)  # 将图像分为b,g,r三部分
        bgr = cv2.merge([b, g, r])  # 按照bgr顺序合并图像
        rgb = cv2.merge([r, g, b])  # 按照rgb顺序合并图像
        pylab.subplot(1, 4, 2)
        pylab.imshow(bgr)
        pylab.subplot(1, 4, 3)
        pylab.imshow(rgb)
        pylab.subplot(1, 4, 4)
        pylab.imshow(lena_double)
        pylab.show()
