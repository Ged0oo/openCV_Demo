import cv2
import numpy as np

def ClickEvent(event, x, y, flages, param):
    font = cv2.FONT_HERSHEY_SIMPLEX

    if(event == cv2.EVENT_LBUTTONDOWN):
        txt = 'X: ' + str(x) + ' Y: ' + str(y)
        cv2.putText(img, txt, (x, y), font, 0.5, (0, 255, 255), 2, cv2.LINE_AA)

    if(event == cv2.EVENT_RBUTTONDOWN):
        blue  = img[y, x, 0]
        green = img[y, x, 1]
        red   = img[y, x, 2] 
        txt = 'B: ' + str(blue) + ' G: ' + str(green) + ' R: ' + str(red)
        cv2.putText(img, txt, (x, y), font, 0.5, (200, 100, 100), 2, cv2.LINE_AA)

    cv2.imshow('image', img)

img = cv2.imread("lena.jpg", -1)
cv2.imshow('image', img)
cv2.setMouseCallback('image', ClickEvent)
cv2.waitKey(0)
cv2.destroyAllWindows()




