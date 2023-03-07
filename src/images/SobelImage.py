import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('../../images/cat.jpg', -1)
laplacian = cv.Laplacian(img, cv.CV_64F)
sobelx = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=5)
sobely = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=5)
plt.subplot(2, 3, 1), plt.imshow(img,  cmap='binary')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 3, 2), plt.imshow(laplacian, cmap='binary')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 3, 3), plt.imshow(sobelx, cmap='binary')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 3, 4), plt.imshow(sobely,  cmap='binary')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

edges = cv.Canny(img, 100, 200)
plt.subplot(2, 3, 5),
plt.imshow(img,  cmap='binary')
plt.title('Original Image')
plt.xticks([]), plt.yticks([])
plt.subplot(2, 3, 6),
plt.imshow(edges, cmap='binary')
plt.title('Edge Image')
plt.xticks([]), plt.yticks([])
plt.show()

