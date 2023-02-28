import cv2
import matplotlib.pyplot as pylab
import numpy as np

class Bisection:
    def PickBisectionMatrix(self):
        image = cv2.imread('../images/black.png')
        print(image.shape[0], image.shape[1], image.shape[2], image.dtype)
        image[50:100, 200:300] = np.random.randint(0, 256, (50, 100, 3))
        image = cv2.cvtColor(image, cv2.GC_BGD)
        lena = cv2.imread("../images/black.png", 0)
        print(lena.shape)
        r = lena.shape[0]
        c = lena.shape[1]
        x = np.zeros((r, c, 8), dtype=np.uint8)
        for i in range(8):
            x[:, :, i] = 2 ** i
        r = np.zeros((r, c, 8), dtype=np.uint8)
        for i in range(8):
            r[:, :, i] = cv2.bitwise_and(lena, x[:, :, i])
            mask = r[:, :, i] > 0
            r[mask] = 255
            pylab.gray()
            pylab.subplot(3, 3, i + 1)
            pylab.imshow(r[:, :, i])
            pylab.axis('off')  # 去掉坐标轴
            pylab.title(str(i + 1))
        pylab.show()
