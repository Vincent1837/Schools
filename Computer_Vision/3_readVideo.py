### imoprt library ###
import numpy as np
import cv2

### Capture from camera or Read an video ###
cap = cv2.VideoCapture('CloudFormationVideo.avi')

### Display the frame ###
while(cap.isOpened()):
    ret, frame = cap.read()
    ### Do the processing (convert RGB to grayscale)###
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # ori = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    ## red = cv2.cvtColor(frame, cv2.)
    cv2.imshow('110502567_蔡淵丞_gray_frame', gray)
    #cv2.imshow('110502567_蔡淵丞_original_frame', ori)
    
    ## if cv2.waitKey(1) & 0xFF == ord('r'):

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

### Close and Exit ###
cap.release()
cv2.destroyAllWindows()


