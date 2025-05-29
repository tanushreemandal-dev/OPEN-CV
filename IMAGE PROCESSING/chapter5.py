import cv2
import numpy as np
width,height=250,350
img=cv2.imread("RESOURCES\Cards.PNG")
imgResize=cv2.resize(img,(450,450))
pst1=np.float32([[399,62],[671,169],[563,665],[281,571]])
pts2=np.float32([[0,0],[width,0],[width,height],[0,height]])
matrix=cv2.getPerspectiveTransform(pst1,pts2)
imgOutput=cv2.warpPerspective(imgResize,matrix,(width,height))
cv2.imshow("Cards",imgResize)
cv2.imshow("Output",imgOutput)
cv2.waitKey(0)
