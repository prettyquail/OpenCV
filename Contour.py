import cv2

img=cv2.imread("Cont.png")
imgray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Second argument is min value ,third argument is max value,fourth argument is type 
# thresh=cv2.threshold(imgray,127,255,0)
edged = cv2.Canny(imgray, 30, 200)


#To find the number of contours
#2 argument is mode,3 argument is method
# contours,hierarchy,a=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
# contours,hierarchy= cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

contours, hierarchy = cv2.findContours(edged, 
    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
  
cv2.imshow('Canny Edges After Contouring', edged)

print("Number of contours"+str(len(contours)))

#drawContours function will draw the boundary around the shapes or words present in the image.
#-1 or index denotes that it will draw the boundaries around the all shapes which is 5 here .
#fourth argument defines the color of boundary
#fifth argument is the value of thickness
cv2.drawContours(img,contours,-1,(0,255,0),3)

cv2.imshow('Image',img)
cv2.imshow('Image GRAY',imgray)
cv2.waitKey(0)
cv2.destroyAllWindows()