# Python code for Multiple Color Detection


import numpy as np
import cv2


# Capturing video through webcam

# Start a while loop
class Detect():
	

	# Reading the video from the
	# webcam in image frames
    def get_frame(self, frame):
    	self.frame = frame

	# Convert the imageFrame in
	# BGR(RGB color space) to
	# HSV(hue-saturation-value)
	# color space
    def detect(self):
        	hsvFrame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)

	# Set range for red color and
	# define mask
        	red_lower = np.array([136, 87, 111], np.uint8)
        	red_upper = np.array([180, 255, 255], np.uint8)
        	red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)

	# Morphological Transform, Dilation
	# for each color and bitwise_and operator
	# between imageFrame and mask determines
	# to detect only that particular color
        	kernal = np.ones((5, 5), "uint8")
        	
        	# For red color
        	red_mask = cv2.dilate(red_mask, kernal)
        	res_red = cv2.bitwise_and(self.frame, self.frame,
        							mask = red_mask)
	


	# Creating contour to track red color
        	contours, hierarchy = cv2.findContours(red_mask,
        										cv2.RETR_TREE,
        										cv2.CHAIN_APPROX_SIMPLE)
        	
        	for pic, contour in enumerate(contours):
        		self.area = cv2.contourArea(contour)
        		if(self.area > 300):
        			x, y, w, h = cv2.boundingRect(contour)
        			imageFrame = cv2.rectangle(self.frame, (x, y),
        									(x + w, y + h),
        									(0, 0, 255), 2)
        			
        			cv2.putText(imageFrame, "Red Colour", (x, y),
        						cv2.FONT_HERSHEY_SIMPLEX, 1.0,
        						(0, 0, 255))	


			
    def show(self, cond=1):
        if cond == 1:
            cv2.imshow("mtrcjr", self.frame)

        else: 
            pass
