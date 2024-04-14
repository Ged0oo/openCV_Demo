import cv2
import numpy as np

def ClickEvent(event, x, y, flages, param):
    font = cv2.FONT_HERSHEY_SIMPLEX

    if(event == cv2.EVENT_LBUTTONDOWN):
        cv2.circle(img, (x, y), 2, [0, 0, 255], -1)
        points.append((x, y))

        if(len(points) > 1) :
            cv2.line(img, points[-1], points[-2], (0, 0, 255), 3)
        
        cv2.putText(img, txt, (x, y), font, 0.5, (0, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow('image', img)

img = cv2.imread("lena.jpg", -1)
cv2.imshow('image', img)
points = [] 
cv2.setMouseCallback('image', ClickEvent)
cv2.waitKey(0)
cv2.destroyAllWindows()




