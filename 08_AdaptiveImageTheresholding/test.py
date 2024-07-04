import cv2 as cv
import numpy as np

import os
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

img = cv.imread('home.jpg', 0)
_, th1 = cv.threshold(img, 50, 255, cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 21, 2)
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 21, 2)

cv.imshow("Image", img)
cv.imshow("TH2", th2)
cv.imshow("TH3", th3)

while(1) :
    k = cv.waitKey(1) & 0xFF
    if k==27 : break

cv.destroyAllWindows()








