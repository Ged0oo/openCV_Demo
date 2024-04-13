import cv2

cap = cv2.VideoCapture(0)

while(1) :
    ret, frame = cap.read()
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame", grey)
    k = (cv2.waitKey(1) & 0xFF) == ord('q')
    if k :
        break

cap.release()
cv2.destroyAllWindows()