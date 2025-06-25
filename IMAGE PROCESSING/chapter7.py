import cv2
import numpy as np
def nothing(x):
    pass
cv2.namedWindow("Trackbar")
cv2.resizeWindow("Trackbar",640,240)
cv2.createTrackbar("Hue Min","Trackbar",1,179,nothing)
cv2.createTrackbar("Hue Max","Trackbar",179,179,nothing)
cv2.createTrackbar("Sat Min","Trackbar",17,255,nothing)
cv2.createTrackbar("Sat Max","Trackbar",255,255,nothing)
cv2.createTrackbar("Val Min","Trackbar",0,255,nothing)
cv2.createTrackbar("Val Max","Trackbar",255,255,nothing)

while(True):
    img=cv2.imread("RESOURCES\image.png")
    imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min=cv2.getTrackbarPos("Hue Min","Trackbar")
    h_max=cv2.getTrackbarPos("Hue Max","Trackbar")
    s_min=cv2.getTrackbarPos("Sat Min","Trackbar")
    s_max=cv2.getTrackbarPos("Sat Max","Trackbar")
    v_min=cv2.getTrackbarPos("Val Min","Trackbar")
    v_max=cv2.getTrackbarPos("Val Max","Trackbar")
    print(h_min,h_max,s_min,s_max,v_min,v_max)

    lower=np.array([h_min,s_min,v_min])
    upper=np.array([h_max,s_max,v_max])
    mask=cv2.inRange(imgHSV,lower,upper)
    imgRes=cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow("Original",img)
    cv2.imshow("HSV",imgHSV)
    cv2.imshow("Mask",mask)
    cv2.imshow("Result",imgRes)
    cv2.waitKey(1)
