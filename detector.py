"""
detector.py
-----------------------
Face Detection Module
"""

import cv2
import os
from datetime import datetime

# PLEASE INSTALL pip install opencv-python==4.12.0.88
class FaceDetector:

    def __init__(self):

        cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"

        self.face_detector = cv2.CascadeClassifier(cascade_path)

        if self.face_detector.empty():
            raise Exception(f"Failed to load Haar Cascade.\nPath: {cascade_path}")

        os.makedirs("captures", exist_ok=True)

    ###########################################################

    def detect(self, frame):

        # Convert to grayscale
        gray = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2GRAY
        )

        # Detect faces
        faces = self.face_detector.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(40, 40)
        )

        # Draw rectangles
        for (x, y, w, h) in faces:

            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

        # Display number of faces
        cv2.putText(
            frame,
            f"Faces: {len(faces)}",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        return frame

    ###########################################################

    def save_frame(self, frame):

        filename = datetime.now().strftime(
            "captures/%Y%m%d_%H%M%S.jpg"
        )

        cv2.imwrite(filename, frame)

        return filename