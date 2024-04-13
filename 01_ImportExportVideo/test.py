import cv2
import datetime

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('out.avi', fourcc, 20.0, (640, 480))

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while(cap.isOpened()) :
    ret, frame = cap.read()

    if ret==True:
        font = cv2.FONT_HERSHEY_SIMPLEX
        txt = 'Width: ' + str(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) + ' Hight: ' + str(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        frame = cv2.putText(frame, txt, (10, 50), font, 1, (0, 255, 255), 2, cv2.LINE_AA)

        date = str(datetime.datetime.now())
        frame = cv2.putText(frame, date, (10, 100), font, 1, (0, 255, 255), 2, cv2.LINE_AA)

        out.write(frame)
        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame", frame)
        
        k = (cv2.waitKey(1) & 0xFF) == ord('q')
        if k : break
    else : break

cap.release()
out.release()
cv2.destroyAllWindows()