"""
app.py
-------------------------
Main application.

This is the main file you run to start the program.
It opens your webcam, looks for faces in the video,
draws boxes around them, and lets you quit or save a picture
by pressing keys on your keyboard.

Responsibilities:
1. Open webcam
2. Read video frames
3. Send each frame to detector.py
4. Display processed frames
5. Handle keyboard commands
"""

import cv2
from detector import FaceDetector


class VisionApp:
    """
    This class controls the whole program.
    Think of it like the "brain" that connects the camera
    and the face detector.
    """

    def __init__(self):
        # create the face detector (it knows how to find faces)
        self.detector = FaceDetector()

        #  open the default webcam (usually camera number 0)
        self.camera = cv2.VideoCapture(0)

        # Check if the camera actually opened
        if not self.camera.isOpened():
            raise Exception("Could not open webcam.")

        # Set the video size to 640x480 (a common small size that runs faster)
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        print("Camera started successfully.")

    ###################################################

    def run(self):
        """
          this is the main loops. it keeps running until   you press ' q'.
        every time through the loop it:
        -grabs one picture (frame) from the camera
        - asks the detector to find faces
         - shows the result on screen
            """

        while True:
            #  read one frame from the camera
             # success = True if it worked, frame = the actual image
            success, frame = self.camera.read()

            if not success:
                print("Failed to read frame.")
                break

           #  send the frame to the detector so it can find faces
            #   and draw green boxes around them.
            processed_frame = self.detector.detect(frame)

            # Show the image in a window
            cv2.imshow("Computer Vision Project", processed_frame)

            # Wait 1 millisecond and check if a key was pressed
            key = cv2.waitKey(1) & 0xFF

                # If the user  pressed 'q', quit the program
            if key == ord("q"):
                break

            # If the user pressed   'c', save the current picture
            elif key == ord("c"):
                filename = self.detector.save_frame(processed_frame)
                print(f"Saved: {filename}")

        # the clean up when the program end
        self.camera.release()          # turn off the camera
        cv2.destroyAllWindows()        # Close all OpenCV windows.


########################################################

    # dis part only runs when you start this file directly
#(not when another file imports it)
if __name__ == "__main__":
    app = VisionApp()
    app.run()
