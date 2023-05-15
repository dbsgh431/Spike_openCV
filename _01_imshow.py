import cv2
import numpy as np

img = np.zeros((255, 255), dtype=np.uint8)

cv2.imshow("window", img)
cv2.waitKey(0)
