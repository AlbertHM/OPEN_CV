import numpy as np 
import cv2
#created a image
img=np.zeros((512,512,3),np.uint8)
# Draw a diagonal blue line with thickness of 5 px
img1=cv2.line(img,(0,0),(511,511),(255,0,0),5)
#now use a frame to show it just as displaying a image
cv2.imshow("Image",img1)
cv2.waitKey(0)           
cv2.destroyAllWindows()

