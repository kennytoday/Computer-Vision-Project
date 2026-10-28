"""
detector.py
-----------------------
Face Detection Module

This file contains the code that actually looks for faces
in each picture from the webcam and draws green boxes around them.
It uses OpenCV's built-in "Haar Cascade" face detector
(a classic, fast method that works pretty well).
"""

import cv2
import os
from datetime import datetime

# Note: Make sure you installed OpenCV with:
# pip install opencv-python==4.12.0.88


class FaceDetector:
    """
    This class knows how to find faces in an image
    and draw boxes around them.
    """

    def __init__(self):
        # OpenCV comes with pre-trained face detection files.
        # This line finds the path to the frontal face detector.
        # cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        
        cascade_path = cv2.data.haarcascades + "haarcascade_eye.xml"

        # Load the face detector
        self.face_detector = cv2.CascadeClassifier(cascade_path)

        # Make sure it loaded correctly
        if self.face_detector.empty():
            raise Exception(f"Failed to load Haar Cascade.\nPath: {cascade_path}")

        # Create a folder called "captures" if it doesn't already exist
        # (this is where saved pictures will go)
        os.makedirs("captures", exist_ok=True)

    ###########################################################

    def detect(self, frame):
        """
        Look for faces in the frame and draw boxes around them.
        Returns the frame with the drawings added.
        """

        # Convert the color image to grayscale.
        # Face detection works better (and faster) on gray images.
        gray = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2GRAY
        )

        # Actually detect the faces
        # scaleFactor = how much the image size is reduced each step
        # minNeighbors = how strict the detector is
        # minSize = smallest face it will look for
        faces = self.face_detector.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(40, 40)
        )

        # Draw a green rectangle around every face that was found
        for (x, y, w, h) in faces:
            cv2.rectangle(
                frame,
                (x, y),                 # top-left corner
                (x + w, y + h),         # bottom-right corner
                (0, 255, 0),            # color (green in BGR)
                2                       # line thickness
            )

        # Write the number of faces on the image (top-left corner)
        cv2.putText(
            frame,
            f"Faces: {len(faces)}",
            (10, 30),                   # position
            cv2.FONT_HERSHEY_SIMPLEX,   # font
            1,                          # size
            (0, 255, 0),                # green color
            2                           # thickness
        )

        return frame

    ###########################################################

    def save_frame(self, frame):
        """
        Save the current frame as a picture file.
        The filename includes the date and time so it is unique.
        """
        filename = datetime.now().strftime(
            "captures/%Y%m%d_%H%M%S.jpg"
        )

        # Write the image to disk
        cv2.imwrite(filename, frame)

        return filename
