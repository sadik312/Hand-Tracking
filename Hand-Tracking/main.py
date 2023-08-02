import cv2 
import mediapipe as mp

# Initialise hand tracking module from mediapipe
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Open webcam for capturing video
cap = cv2.VideoCapture(2)

# Create loop to read frames from webcam
while True:
    ret, frame = cap.read()
    if not ret:
        break
    # use mp_hands module to detect hands in each frame and track
    with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
        # convert img BGR to RGB
        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(image_rgb)
        
        # If hands are detected, draw landmarks on hands
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame, hand_landmarks, mp_hands.HAND_CONNECTIONS
                )
                
    # Display frame with hand landmarks
    cv2.imshow('Hand Tracking', frame)
    if cv2.waitKey(1) & 0xFF == 27: # 'Esc' to exit
        exit

cap.release()
cv2.destroyAllWindows()
