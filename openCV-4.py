#!/usr/bin/env python3

# Pauls solution to lesson 6 homework
### doesn't work well with my webcam because my max resolution is too small
#### asks user for input and displays user specified number of rows and columns
import cv2

print(cv2.__version__)

rows = int(input("Boss, how many rows do you want? "))
columns = int(input("How many columns? "))


width = 640
height = 320 

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    ignore, frame = cam.read()
    frame = cv2.resize(frame, (int(width/columns), int(height/columns)))
    for i in range(rows):
        for j in range(columns):
            windName = 'Window' + str(i) + ' x ' + str(j)
            cv2.imshow(windName, frame)
            cv2.moveWindow(windName, int(width/columns)*j, int(height/columns+30)*i)


    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()