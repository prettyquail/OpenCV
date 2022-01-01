from cv2 import cv2
img=cv2.imread("m.png")

imgBlur=cv2.GaussianBlur(img,(7,7),0)
cv2.imshow("Gray image",imgBlur)
cv2.waitKey(0)
        
        