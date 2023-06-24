import cv2
import mediapipe as mediapipe

# initialise hand tracking module
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# initialise video capture with webcam
cap = cv2.VideoCapture(0)