#!/usr/bin/env python3
import cv2
print(cv2.__version__)

width = 640
height = 480
myRadius = 30
myColor = (0, 0, 0)
myThickness = 2
myText = 'My text'

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    ignore,  frame = cam.read()
    # frame[200:280, 260: 380] = (255, 0, 0)
    cv2.rectangle(frame, (260, 200), (380, 280), (0, 255, 0), 1)
    cv2.circle(frame, (int(width/2), int(height/2)),
               myRadius, myColor, myThickness)
    cv2.putText(frame, myText, (40, 60),
                cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 1)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam', 0, 0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()
