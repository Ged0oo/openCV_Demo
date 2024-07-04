import cv2 as cv
import numpy as np

import os
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

img = cv.imread('gradient.png', 0)
_, th1 = cv.threshold(img, 50, 255, cv.THRESH_BINARY)
_, th2 = cv.threshold(img, 200, 255, cv.THRESH_BINARY_INV)
_, th3 = cv.threshold(img, 20, 255, cv.THRESH_TRUNC)
_, th4 = cv.threshold(img, 200, 255, cv.THRESH_TOZERO)
_, th5 = cv.threshold(img, 200, 255, cv.THRESH_TOZERO_INV)

cv.imshow("Image", img)
cv.imshow("TH1", th1)
cv.imshow("TH2", th2)
cv.imshow("TH3", th3)
cv.imshow("TH4", th4)
cv.imshow("TH5", th5)

while(1) :
    k = cv.waitKey(1) & 0xFF
    if k==27 : break

cv.destroyAllWindows()