#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 16:47:42 2022

@author: fuchs
"""
import cv2
from c_detec_try import Detect

webcam = cv2.VideoCapture(0)

d = Detect()
while(1):
    ret, frame = webcam.read()
    d.get_frame(frame)
    d.detect()
    d.show()
    if cv2.waitKey(10) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
