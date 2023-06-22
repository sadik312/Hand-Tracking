import cv2
import mediapipe as mp
import time # to check the framerate

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    success, img = cap.read() # will give frame

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
    results = hands.process(imgRGB)
    # if hand is present, print coordinates of landmarks of hand
    print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) == ord('q'): #press q to exit
        break

cap.release()
cv2.destroyAllWindows()
