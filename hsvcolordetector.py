# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 18:26:10 2022

@author: DevRehamMetwally
"""

import cv2
import numpy as np


def empty(a):
    pass

cap = cv2.VideoCapture(0)


cv2.namedWindow("HSV")
cv2.resizeWindow("HSV",640,300)
cv2.createTrackbar("HUE MIN","HSV",0,179,empty)
cv2.createTrackbar("HUE MAX","HSV",179,179,empty)

cv2.createTrackbar("SAT MIN","HSV",0,255,empty)
cv2.createTrackbar("SAT MAX","HSV",255,255,empty)

cv2.createTrackbar("VALUE MIN","HSV",0,255,empty)
cv2.createTrackbar("VALUE MAX","HSV",255,255,empty)

while cap.isOpened():
    _,frame = cap.read()
    if _:
        
        
        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        
        h_min = cv2.getTrackbarPos("HUE MIN","HSV")
        h_max = cv2.getTrackbarPos("HUE MAX","HSV")
        
        s_min = cv2.getTrackbarPos("SAT MIN","HSV")
        s_max = cv2.getTrackbarPos("SAT MAX","HSV")
        
        v_min = cv2.getTrackbarPos("VALUE MIN","HSV")
        v_max = cv2.getTrackbarPos("VALUE MAX","HSV")
        
        lower = np.array([h_min,s_min,v_min])
        upper = np.array([h_max,s_max,v_max])
        
        mask = cv2.inRange(frame,lower,upper)
        result  = cv2.bitwise_and(frame,frame,mask=mask)
        
        
        cv2.imshow("Video",frame)
        cv2.imshow("Mask",mask)
        cv2.imshow("Result",result)
        
        
        if cv2.waitKey(5) & 0xFF == 27:
            break
    else:
        break
    
    
    
cap.release()
cv2.destroyAllWindows()