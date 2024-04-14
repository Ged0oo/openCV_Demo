import cv2
import numpy as np

def ClickEvent(event, x, y, flages, param):
    if(event == cv2.EVENT_LBUTTONDOWN):
        print(x, '   ', y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        txt = 'X: ' + str(x) + ' Y: ' + str(y)
        cv2.putText(img, txt, (x, y), font, 1, (0, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow('image', img)


img = np.zeros((512, 512, 3), np.uint8)
cv2.imshow('image', img)
cv2.setMouseCallback('image', ClickEvent)
cv2.waitKey(0)
cv2.destroyAllWindows()