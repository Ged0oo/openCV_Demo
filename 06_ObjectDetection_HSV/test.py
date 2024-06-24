import cv2
import numpy as np

def nothing(x) :
    pass

cv2.namedWindow("Tracking")
cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)
cv2.createTrackbar("UH", "Tracking", 255, 255, nothing)
cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)
cv2.createTrackbar("US", "Tracking", 255, 255, nothing)
cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)
cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)


while(1) :
    frame = cv2.imread('test.jpg')

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h = cv.getTrackbarPos('LH', 'Tracking')
    u_h = cv.getTrackbarPos('UH', 'Tracking')
    l_s = cv.getTrackbarPos('LS', 'Tracking')
    u_s = cv.getTrackbarPos('US', 'Tracking')
    l_v = cv.getTrackbarPos('LV', 'Tracking')
    u_v = cv.getTrackbarPos('UV', 'Tracking')


    mask = cv2. inRange(hsv, l_b, u_b)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    k = cv2.waitKey(1) & 0xFF
    if k==27 : break

cv2.destroyAllWindows()