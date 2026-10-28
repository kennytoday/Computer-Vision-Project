"""
detector.py
Detects both Face Masks and Cigarettes using two YOLOv8 models
"""

import cv2
import os
from datetime import datetime
from ultralytics import YOLO
os.environ["YOLO_VERBOSE"] = "False"


class FaceDetector:

    def __init__(self):
        print("Loading models...")

        # Load both models
        # Change the filenames if your files have different names
        self.mask_model = YOLO("mask_model.pt")        # your face mask model
        self.cigarette_model = YOLO("cigarette.pt")    # your cigarette model

        print("Models loaded.")
        os.makedirs("captures", exist_ok=True)

    def detect(self, frame):
        # Run both models
        mask_results = self.mask_model(frame, verbose=False)
        cig_results = self.cigarette_model(frame, verbose=False)

        # Start with the original frame
        annotated_frame = frame.copy()

        # Draw mask detections
        annotated_frame = mask_results[0].plot(img=annotated_frame)

        # Draw cigarette detections on top
        annotated_frame = cig_results[0].plot(img=annotated_frame)

        # Count total detections
        mask_count = len(mask_results[0].boxes) if mask_results[0].boxes is not None else 0
        cig_count = len(cig_results[0].boxes) if cig_results[0].boxes is not None else 0

        cv2.putText(
            annotated_frame,
            f"Masks: {mask_count} | Cigarettes: {cig_count}",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

        return annotated_frame

    def save_frame(self, frame):
        filename = datetime.now().strftime("captures/%Y%m%d_%H%M%S.jpg")
        cv2.imwrite(filename, frame)
        return filename