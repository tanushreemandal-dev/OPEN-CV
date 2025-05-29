import cv2

img=cv2.imread("RESOURCES\image.png")

#converting to greyscale image
imgGrey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#blurring the image
imgBlur=cv2.GaussianBlur(imgGrey,(7,7),0)
#Canny edge detector
imgCanny=cv2.Canny(img,50,150)
imgCanny1=cv2.Canny(img,500,300)

cv2.imshow("Grey image",imgGrey)
cv2.imshow("Blur image",imgBlur)
cv2.imshow("canny image",imgCanny)
cv2.imshow("canny image1",imgCanny1)
cv2.waitKey(0)
