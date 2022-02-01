#!/usr/bin/env python3

import cv2

print(cv2.__version__)
cam = cv2.VideoCapture(0)

while True:
    ignore, frame = cam.read()
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('my web_cam', frame)
    cv2.imshow('my gray_cam', grayFrame)
    cv2.imshow('my web_cam2', frame)
    cv2.imshow('my gray_cam2', grayFrame)
    cv2.moveWindow('my web_cam', 0, 0)
    cv2.moveWindow('my gray_cam', 645, 0)
    cv2.moveWindow('my web_cam2', 645, 550)
    cv2.moveWindow('my gray_cam2', 0, 550)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()