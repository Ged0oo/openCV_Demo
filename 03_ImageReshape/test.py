import cv2
import numpy as np

def ClickEvent(event, x, y, flages, param):
    if(event == cv2.EVENT_LBUTTONDOWN):
        cv2.circle(img, (x, y), 2, [0, 0, 255], -1)
    cv2.imshow('image', img)

img  = cv2.imread("test.jpg")
img2 = cv2.imread("lena.jpg")
final = cv2.add(img, img2)

img  = cv2.resize(img ,  (512, 512))
img2 = cv2.resize(img2,  (512, 512))

cv2.imshow("image", final)
cv2.setMouseCallback('image', ClickEvent)

k = cv2.waitKey(0)
cv2.destroyAllWindows()