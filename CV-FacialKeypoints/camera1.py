# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 18:29:42 2017

@author: shubra
"""

## Add face and eye detection to this laptop camera function 
# Make sure to draw out all faces/eyes found in each frame on the shown video feed

import cv2
import time 

# wrapper function for face/eye detection with your laptop camera
def laptop_camera_go():
    
    # ADDED BY SHUBRA 
    face_cascade = cv2.CascadeClassifier('detector_architectures/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('detector_architectures/haarcascade_eye.xml')
    # END OF ADDITION  BY SHUBRA
    # Create instance of video capturer
    cv2.namedWindow("face detection activated")
    vc = cv2.VideoCapture(0)
    

     #Try to get the first frame
    if vc.isOpened(): 
     rval, frame = vc.read()
#     while rval:
#   
#        # ADDED BY SHUBRA
#        rval, frame = vc.read()
#        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#        faces = face_cascade.detectMultiScale(gray,  1.25, 6)
#        
#        for (x,y,w,h) in faces:
#            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
#            eye_gray = gray[y:y+h, x:x+w]
#            image_frame = frame[y:y+h, x:x+w]
#            
#            eyes = eye_cascade.detectMultiScale(eye_gray)
#            for (ex,ey,ew,eh) in eyes:
#                cv2.rectangle(image_frame,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
#        
#        # END OF ADDITION  BY SHUBRA
#        # Plot the image from camera with all the face and eye detections marked
#        cv2.imshow("face detection activated", frame)
#        
#        # Exit functionality - press any key to exit laptop video
#        key = cv2.waitKey(30)
#        if key > 0: # Exit by pressing any key
#            # Destroy windows 
#            cv2.destroyAllWindows()
#            
#            # Make sure window closes on OSx
#            for i in range (1,5):
#                cv2.waitKey(1)
#            return
#        
#        # Read next frame
#        time.sleep(0.05)             # control framerate for computation - default 20 frames per sec
#        rval, frame = vc.read()   
        
    else:
#        rval = False
        rval, frame = vc.read()
    
    # Keep the video stream open
    while rval:
#    while 1:
        # ADDED BY SHUBRA
        rval, frame = vc.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,  1.25, 6)
        
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            eye_gray = gray[y:y+h, x:x+w]
            image_frame = frame[y:y+h, x:x+w]
            
            eyes = eye_cascade.detectMultiScale(eye_gray)
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(image_frame,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        
        # END OF ADDITION  BY SHUBRA
        # Plot the image from camera with all the face and eye detections marked
        cv2.imshow("face detection activated", frame)
        
        # Exit functionality - press any key to exit laptop video
        key = cv2.waitKey(30)
        if key > 0: # Exit by pressing any key
            # Destroy windows 
            cv2.destroyAllWindows()
            
            # Make sure window closes on OSx
            for i in range (1,5):
                cv2.waitKey(1)
            return
        
        # Read next frame
        time.sleep(0.05)             # control framerate for computation - default 20 frames per sec
        rval, frame = vc.read()    
        
laptop_camera_go()