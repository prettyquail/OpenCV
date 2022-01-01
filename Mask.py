import numpy as np
import cv2

def empty():
    pass

path='car.jpg'

#This will create window for the trackbar result
cv2.namedWindow("TrackBars")

#It will define size of hue resizing window
cv2.resizeWindow("TrackBars",640,250)

#Here we set the initial values after calculating it from the trackbars. First we start from the 0,179,0,255,0,255 as the initial values.
cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)
cv2.createTrackbar("Hue Max","TrackBars",33,179,empty)
cv2.createTrackbar("Sat Min","TrackBars",166,255,empty)
cv2.createTrackbar("Sat Max","TrackBars",255,255,empty)
cv2.createTrackbar("Val Min","TrackBars",0,255,empty)
cv2.createTrackbar("Val Max","TrackBars",255,255,empty)


while True:
    img=cv2.imread('car.jpg')

    imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min=cv2.getTrackbarPos("Hue Min","TrackBars")
    h_max=cv2.getTrackbarPos("Hue Max","TrackBars")
    s_min=cv2.getTrackbarPos("Sat Min","TrackBars")
    s_max=cv2.getTrackbarPos("Sat Max","TrackBars")
    v_min=cv2.getTrackbarPos("Val Min","TrackBars")
    v_max=cv2.getTrackbarPos("Val Max","TrackBars")
    print(h_min,h_max,s_min,s_max,v_min,v_max)

    lower=np.array([h_min,s_min,v_min])
    upper=np.array([h_max,s_max,v_max])
    
    mask=cv2.inRange(imgHSV,lower,upper)

    #The color we need will be only present in the image.
    imgResult=cv2.bitwise_and(img,img,mask=mask)


    cv2.imshow("Original",img)
    cv2.imshow("HSV",imgHSV)
    cv2.imshow("Mask",mask)
    cv2.imshow("Image Result",imgResult)
    cv2.waitKey(1)