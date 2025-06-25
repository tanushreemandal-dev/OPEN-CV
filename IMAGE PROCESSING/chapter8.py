import cv2
import numpy as np

def getContour(img):
    contours,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area=cv2.contourArea(cnt)
        print(area)
        cv2.drawContours(imgContours,cnt,-1,(255,0,0),3)
        
img=cv2.imread(r"RESOURCES\shapes.png")
imgGrey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(imgGrey,(5,5),1)
imgCanny=cv2.Canny(imgBlur,50,150)
imgContours=img.copy()
getContour(imgCanny)
cv2.imshow("Original",img)
cv2.imshow("Grayscale",imgGrey)
cv2.imshow("Blurred",imgBlur)
cv2.imshow("Canny",imgCanny)
cv2.imshow("Contours",imgContours)
cv2.waitKey(0)
