### Import library ###
import cv2
import numpy as np

### Read the image ###
img = cv2.imread('littleMINI.jpg')
### Do the processing ###
row, cols, channels = img.shape
b, g, r = cv2.split(img)
gray = 0.114 * b + 0.587 * g + 0.299 * r
gray = gray.astype(np.uint8)

### Show the image ###
cv2.imshow("gray", gray)
cv2.imshow('image',img)

### Close and exit ###
cv2.waitKey(0)
cv2.destroyAllWindows()





