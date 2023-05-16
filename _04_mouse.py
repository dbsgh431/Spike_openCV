import numpy as np
import cv2

def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print('Left btn pressed')
    if event == cv2.EVENT_RBUTTONDOWN:
        print('right btn pressed')
    if event == cv2.EVENT_LBUTTONUP:
        print('Left btn up')
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print('Left btn double cliked')


img = np.full((300, 300), 255, np.uint8)

title = "window"
cv2.imshow(title, img)

cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()