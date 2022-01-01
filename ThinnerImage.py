import cv2 
import numpy as np 
img = cv2.imread('m.png', 0) 
  
kernel = np.ones((5,5), np.uint8) 

#I get the error that cv2.cv2 has no attribute eroded,because it is erode not eroded
img_erosion = cv2.erode(img, kernel, iterations=1) 
cv2.imshow('Erosion', img_erosion) 
cv2.waitKey(0) 