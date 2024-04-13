import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('out.avi', fourcc, 20.0, (640, 480))

while(cap.isOpened()) :
    ret, frame = cap.read()

    if ret==True:
        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        hight = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

        out.write(frame)

        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame", grey)
        
        k = (cv2.waitKey(1) & 0xFF) == ord('q')
        if k : break
    else : break

cap.release()
out.release()
cv2.destroyAllWindows()