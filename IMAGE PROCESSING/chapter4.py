import numpy as np
import cv2
img=np.zeros((512,512,3),np.uint8)
# img[0:200,300:500]=[0,0,255]
#line
cv2.line(img,(0,0),(511,511),(0,255,0),3)
#rectange
cv2.rectangle(img,(0,0),(250,350),(255,0,255),2)
#cv2.rectangle(img,(0,0),(250,350),(0,0,255),cv2.FILLED)
#circle
cv2.circle(img,(255,255),50,(255,123,0),4)

#text
cv2.putText(img,"  TANU ",(350,200),cv2.FONT_HERSHEY_DUPLEX,0.7,(255,255,255),1)
cv2.imshow("Image",img)
cv2.waitKey(0)
