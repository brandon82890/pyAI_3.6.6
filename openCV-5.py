#!/usr/bin/env python3
import cv2
import numpy as np
print(cv2.__version__)

# TODO: make a checkerboard, 75 pixels per square, 8x8
black = (0, 0, 0)
white = (255, 255, 255)
square = 75

while True:
    frame = np.zeros([600, 600, 3], dtype=np.uint8)
    cv2.imshow('My Window', frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
