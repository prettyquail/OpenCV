import numpy as np
from cv2 import cv2
img = cv2.imread('m.png')
print(img.shape)

imgResize=cv2.resize(img,(300,200))

cv2.imshow("Image",img)
cv2.imshow("Image resize",imgResize)

cv2.waitKey(0)