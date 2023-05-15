import numpy as np
import cv2

img = np.zeros((200, 400), np.uint8)
img[:] = 200

cv2.namedWindow('window1')
cv2.moveWindow('window1', 0, 0)

cv2.imshow('window1', img)
cv2.waitKey(0)
cv2.destroyAllWindows()