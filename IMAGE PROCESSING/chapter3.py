import cv2
import numpy as np

img=cv2.imread("RESOURCES\image.png")
#resize
imgresize=cv2.resize(img,(200,250))
#crop
imgCrop=img[0:200,200:300]
print(img.shape)
#print(imgresize.shape)
print(imgCrop.shape)
cv2.imshow("Original Image", img)
#cv2.imshow("Resize Image", imgresize)
cv2.imshow("Crop Image", imgCrop)
cv2.waitKey(0)

