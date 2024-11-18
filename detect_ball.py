import cv2
import numpy as np 

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if ret is None:
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (17,17), 0)
    circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1.2, 20000, param1=100, param2=42, minRadius=52, maxRadius=300 )

    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
        
            cv2.circle(frame, (i[0], i[1]), 1, (0,0,255), 2)
            cv2.circle(frame, (i[0], i[1]), i[2], (0,255,0), 2)


    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()

