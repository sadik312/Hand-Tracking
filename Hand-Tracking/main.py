import cv2
import mediapipe as mediapipe

# initialise hand tracking module
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# initialise video capture with webcam
cap = cv2.VideoCapture(0)

with mp_hands.hands(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
) as hands:
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            print("Failed to read video")
            break

        # convert image from bgr to rgb
        image = cv2.cvtColor(frame, cv2.COLOR_GBR2RGB)
