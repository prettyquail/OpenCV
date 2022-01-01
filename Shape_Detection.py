import numpy as np
import cv2

img=cv2.imread('shapes.png')
imgGrey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#threshold(src, thresh, maxval, type, dst=None)
_,thrash=cv2.threshold(imgGrey,240,255,cv2.THRESH_BINARY)

#Simple  method to find the all contours
#findContours(image, mode, method, contours=None, hierarchy=None, offset=None)
contours,_=cv2.findContours(thrash,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

for contour in contours:

    #approxPolyDP-This method approx the polygonal curves with a specific precision[approxPolyDP(curve, epsilon, closed, approxCurve=None)]
    #1 argument-curve
    #2 argument-epsilon which is the parameter specifying the approximation accuracy
    #arclength-calculates the curve length
    #True denotes closed shapes
    approx=cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)

    #drawContours(image, contours, contourIdx, color, thickness=None, lineType=None, hierarchy=None, maxLevel=None, offset=None)
    cv2.drawContours(img,[approx],0,(255,160,100),3)

    #x and y coordinates are the position of name of shapes
    x=approx.ravel()[0]
    y=approx.ravel()[1]-5
    if len(approx)==3:
        #putText(img, text, org, fontFace, fontScale, color, thickness=None, lineType=None, bottomLeftOrigin=None)
        cv2.putText(img,"Triangle",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
    elif len(approx)==4:
        x,y,w,h=cv2.boundingRect(approx)
        aspectRatio=float(w)/h
        print(aspectRatio)
        if aspectRatio>=0.95 and aspectRatio<=1.05:
            cv2.putText(img,"Square",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
        else:
            cv2.putText(img,"Rectangle",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
    elif len(approx)==5:
        cv2.putText(img,"Pentagon",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
    elif len(approx)==10:
        cv2.putText(img,"Star",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
    else:
        cv2.putText(img,"Circle",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))



cv2.imshow("shapes",img)
cv2.waitKey(0)
cv2.destroyAllWindows()