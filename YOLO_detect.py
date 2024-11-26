

from ultralytics import YOLO
import cv2
import math
import cvzone

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

model = YOLO(r"mini project\yolov5\yolov5-env\best (3).pt")
Classnames = ['red ball']
while True:
    ret, frame = cap.read()
    result = model(frame, stream=True)
    for r in result:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5 )
            conf = math.ceil((box.conf[0]*100))/100
            cls = int(box.cls[0])
            cvzone.putTextRect(frame, f'{Classnames[cls]} {conf}', (max(0, x1), max(35, y1)))
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) == ord('q'):
        break