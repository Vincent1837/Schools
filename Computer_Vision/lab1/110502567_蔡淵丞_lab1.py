### imoprt library ###
import numpy as np
import cv2

### Capture from camera or Read an video ###
cap = cv2.VideoCapture('minion_video.avi')

### Display the frame ###
while(cap.isOpened()):
    ret, frame = cap.read()
    ### Do the processing (convert RGB to grayscale)###
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    red_color = np.array([0, 0, 255])
    red_frame = frame * red_color
    red_frame = red_frame.astype(np.uint16)

    green_color = np.array([0, 255, 0])
    green_frame = frame * green_color
    green_frame = green_frame.astype(np.uint16)

    blue_color = np.array([255, 0, 0])
    blue_frame = frame * blue_color
    blue_frame = blue_frame.astype(np.uint16)

    cv2.imshow('110502567_蔡淵丞_gray_frame', gray)
    cv2.imshow('110502567_蔡淵丞_origin_frame', frame)
    
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    if key == ord('r'):
        cv2.imshow('110502567_蔡淵丞_Capture_r', red_frame)
        img_write = cv2.imencode('.png', red_frame)[1].tofile('110502567_蔡淵丞_Capture_r.png')
    if key == ord('g'):
        cv2.imshow('110502567_蔡淵丞_Capture_g', green_frame)
        img_write = cv2.imencode('.png', green_frame)[1].tofile('110502567_蔡淵丞_Capture_g.png')
    if key == ord('b'):
        cv2.imshow('110502567_蔡淵丞_Capture_b', blue_frame)
        img_write = cv2.imencode('.png', blue_frame)[1].tofile('110502567_蔡淵丞_Capture_b.png')


### Close and Exit ###
cap.release()
cv2.destroyAllWindows()
