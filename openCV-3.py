#!/usr/bin/env python3

import cv2

print(cv2.__version__)

# screen size 3840x1080 double monitor
# can have 48 windows this size 
width=320
height=240

cam = cv2.VideoCapture(0) 
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

# loop to create and position screens
while True:
    ignore, frame = cam.read()
    x = 0
    y = 0

    for n in range(51):
        if x <= 3520:
            cv2.imshow('web_cam{}'.format(n), frame)
            cv2.moveWindow('web_cam{}'.format(n),x, y)
            x += 320
        elif y <= 840:
            x=0
            y += 240
            cv2.imshow('web_cam{}'.format(n), frame)
            cv2.moveWindow('web_cam{}'.format(n), x, y)
        else:
            break
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()