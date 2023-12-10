import cv2 as cv
import numpy as np



vid = cv.VideoCapture('vtest.avi')

while(vid.isOpened()):
    #Capture frame by frame
    ret, frame = vid.read()

    #display the resulting frame
    cv.imshow('frame',frame)
    key = cv.waitKey(1000) 
    if key ==  27: #wait for ESc key to exit
        break


#when everything is done, release the capture
# syntax: object.release()
vid.release()
cv.destroyAllWindows()
