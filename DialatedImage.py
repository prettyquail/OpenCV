from cv2 import cv2
import numpy as np
img=cv2.imread("m.png")


Kernel=np.ones((5,5),np.uint8) #(3,3) is matrix

imgCanny=cv2.Canny(img,150,200)
imgDialation=cv2.dilate(imgCanny,Kernel,iterations=1)
cv2.imshow("Canny image",imgDialation)
cv2.waitKey(0)
        
        