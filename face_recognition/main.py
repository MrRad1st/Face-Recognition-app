import threading
import cv2
from deepface import DeepFace
from pathlib import Path
# import os
from os import path

current_dir = Path.cwd()
print(current_dir)


cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0
face_match = False

img_path = path.join(str(current_dir)+"img.png")

try:
    img = cv2.imread(img_path)
except FileNotFoundError:
    print("Error: Image file not found!")




print(str(current_dir))
reference_image = cv2.imread(img_path)