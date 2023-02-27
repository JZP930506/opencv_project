import cv2

cv2.namedWindow('video',cv2.WINDOW_NORMAL)
cv2.resizeWindow('video',640,480)

cap=cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame=cap.read()
    if not ret:
        break
    cv2.imshow('video',frame)

    key=cv2.waitKey(10)
    if key& 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

