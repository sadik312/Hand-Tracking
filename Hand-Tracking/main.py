import cv2
import mediapipe as mp
import time # to check the framerate

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read() # will give frame
    
    cv2.imshow("Image, img")
    cv2.waitKey(0)
