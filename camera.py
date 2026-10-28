"""
camera.py
---------------------
Handles webcam operations.

This file is a simple helper that opens the webcam
and gives you frames (pictures) from it.
In the current project the main app.py opens the camera itself,
but this class is useful if you want to keep camera code separate.
"""

import cv2


class Camera:
    """
    A simple class that talks to your webcam.
    """

    def __init__(self, camera_index=0):
        # camera_index=0 means the first/default webcam on your computer
        self.cap = cv2.VideoCapture(camera_index)

        # Make sure the camera opened correctly
        if not self.cap.isOpened():
            raise Exception("Unable to open webcam.")

        # Set the size of the video (width and height)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    ####################################################

    def read(self):
        """
        Grab one frame (picture) from the camera.
        Returns:
            success (True/False) and the frame itself
        """
        success, frame = self.cap.read()
        return success, frame

    ####################################################

    def release(self):
        """
        Turn the camera off when you're done.
        Always do this so the camera doesn't stay locked.
        """
        self.cap.release()
