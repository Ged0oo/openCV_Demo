import cv2 as cv
import numpy as np

img = cv.imread('gradient.png', 0)
cv.imshow("Image", img)

while(1) :
    k = cv.waitKey(1) & 0xFF
    if k==27 : break

cv.destroyAllWindows()