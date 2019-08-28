import cv2
import numpy as np
import sys
import keyboard
import base64
import time
cap = cv2.VideoCapture(0)

while(1):

    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_yellow = np.array([18, 94, 140])
    upper_yellow = np.array([48, 255, 255])
    
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    res = cv2.bitwise_and(frame,frame, mask= mask)
    edges = cv2.Canny(mask, 75, 150)
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 50, maxLineGap=50)

    #cv2.imshow('Original',frame)
    edges = cv2.Canny(frame,100,200)
    #cv2.imshow('Edges',edges)

    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
    #cv2.imshow("frame", frame)
    #cv2.imshow("edges", edges)
    retval, buffer = cv2.imencode('.jpeg',frame)
    jpegtext = base64.b64encode(buffer).decode()
        
    print(jpegtext)
    if keyboard.is_pressed('q'):
        break

cv2.destroyAllWindows()
cap.release()
