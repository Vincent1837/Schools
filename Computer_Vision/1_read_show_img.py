### Import OpenCV ###
import cv2
import numpy as np

### Read the image ###
img = cv2.imread('littleMINI.jpg', cv2.IMREAD_GRAYSCALE)
### Do the processing ###
### Show the image ###
cv2.imshow('image',img)
### Close and exit ###
cv2.waitKey(0)
cv2.destroyAllWindows()