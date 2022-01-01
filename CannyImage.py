from cv2 import cv2
img=cv2.imread("m.png")

imgCanny=cv2.Canny(img,150,200)
cv2.imshow("Canny image",imgCanny)
cv2.waitKey(0)
        
        