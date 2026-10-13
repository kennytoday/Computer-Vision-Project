"""
app.py
-------------------------
Main application.

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

    def __init__(self):

        # Create detector
        self.detector = FaceDetector()

        # Open default webcam
        self.camera = cv2.VideoCapture(0)

        if not self.camera.isOpened():
            raise Exception("Could not open webcam.")

        # Camera settings
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        print("Camera started successfully.")

    ###################################################

    def run(self):

        while True:

            success, frame = self.camera.read()

            if not success:
                print("Failed to read frame.")
                break

            # Send frame to detector
            processed_frame = self.detector.detect(frame)

            # Show result
            cv2.imshow("Computer Vision Project", processed_frame)

            key = cv2.waitKey(1) & 0xFF

            # Quit
            if key == ord("q"):
                break

            # Save current frame
            elif key == ord("c"):

                filename = self.detector.save_frame(processed_frame)

                print(f"Saved: {filename}")

        self.camera.release()

        cv2.destroyAllWindows()


########################################################

if __name__ == "__main__":

    app = VisionApp()

    app.run()