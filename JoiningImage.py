import cv2
import numpy as np
img=cv2.imread("cards.jpg")

imgHor=np.hstack((img,img))
imgVer=np.vstack((img,img))

cv2.imshow("Image",imgHor)
cv2.imshow("Output",imgVer)
cv2.waitKey(0)