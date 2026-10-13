"""
camera.py
---------------------
Handles webcam operations.
"""

import cv2


class Camera:

    def __init__(self, camera_index=0):

        self.cap = cv2.VideoCapture(camera_index)

        if not self.cap.isOpened():
            raise Exception("Unable to open webcam.")

        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    ####################################################

    def read(self):

        success, frame = self.cap.read()

        return success, frame

    ####################################################

    def release(self):

        self.cap.release()