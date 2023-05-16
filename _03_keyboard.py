import numpy as np
import cv2

try:
    from cv2 import cv2
except ImportError:
    pass
key_case = {
    ord('a') : "a pressed",
    ord('d') : "d pressed",
    ord('s') : "s pressed",
    ord('w') : "w pressed",
}

img = np.ones((200, 300), np.float32)
cv2.namedWindow('keyboardEvent')
cv2.imshow('keyboardEvent', img)



while True:


    key = cv2.waitKeyEx(100)

    if key == 27:
        break

    try:
        result = key_case[key]
        print(result)
    except:
        result = -1


cv2.destroyAllWindows()
