#!/usr/bin/env python3
import cv2
import numpy as np

# this script makes a checkerboard pattern of user defined size
boardSize = int(input("What size is your board? "))
numSquares = int(input("How many squares? "))
squareSize = int(boardSize/numSquares)

darkColor = (0, 0, 0)
lightColor = (175, 175, 175)
nowColor = darkColor

while True:
    x = np.zeros([boardSize, boardSize, 3], dtype=np.uint8)

    for row in range(0, numSquares):
        for column in range(0, numSquares):
            x[squareSize*row:squareSize *
                (row+1), squareSize*column:squareSize*(column+1)] = nowColor
            if nowColor == darkColor:
                nowColor = lightColor
            else:
                nowColor = darkColor
        if nowColor == darkColor:
            nowColor = lightColor
        else:
            nowColor = darkColor

    cv2.imshow('My Checkerboard', x)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
