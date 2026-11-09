Computer Vision Project: Real-Time Object Detection Using YOLOv8 and OpenCV

1. Project Overview

This project is a Python-based computer vision application that uses deep learning to detect face masks and cigarettes through a webcam.

I developed the application using YOLOv8 and OpenCV, integrating two separately trained object detection models into a single detection workflow. The application processes live camera frames, identifies objects recognised by the models, displays detection results and allows images to be saved for later review.

The project gave me practical experience in working with trained computer vision models and understanding how object detection can be incorporated into a functional Python application.

2. Background and Motivation

I became interested in computer vision because of its ability to help computers interpret visual information and recognise objects in their surroundings.

I wanted to move beyond learning machine learning concepts theoretically and gain practical experience in building an application that could process real-time visual input.

I chose face-mask and cigarette detection as two different object recognition tasks. Both provided an opportunity to understand how trained models identify visual patterns and how their predictions can be presented through an application.

My interest also extends to the potential use of computer vision in healthcare environments, particularly environmental safety and infection prevention. This project provided an initial opportunity to explore some of the underlying technologies that could support such applications.

3. Project Objectives

The main objectives were to:

- Gain practical experience with computer vision and object detection.
- Work with YOLOv8 models for identifying specific objects.
- Use OpenCV to capture and process webcam video.
- Integrate two independently trained detection models into one application.
- Display detected objects and their counts on live video frames.
- Allow users to capture and save processed images.
- Understand the practical challenges and limitations of automated visual recognition.

4. Technologies and Tools

Technology| How it was used
Python| Application development
YOLOv8 (Ultralytics)| Object detection
OpenCV| Webcam access, frame processing and image display
Roboflow| Dataset preparation and model workflow
PyTorch| Deep learning framework used by the Ultralytics models

5. How the Application Works

The application brings together two YOLOv8 models, each responsible for a different detection task.

Face-mask detection: The first model analyses camera frames to identify face-mask-related objects.

Cigarette detection: The second model analyses the same frames to identify cigarette-related objects.

Both models process each captured frame. Their detection results are drawn onto the original image, allowing the application to display the combined results in one window.

The application also displays the number of detections returned by each model.

The main processing sequence is:

1. The application opens the computer's default webcam.
2. OpenCV captures a video frame.
3. The frame is passed to the face-mask detection model.
4. The same frame is passed to the cigarette detection model.
5. Both sets of results are drawn onto the image.
6. The annotated frame is displayed with detection counts.
7. The user can continue monitoring, save an image or close the application.

6. Dataset Preparation and Model Development

I used Roboflow as part of the dataset preparation and model development workflow.

The original project documentation records approximately:

- 800 images for the face-mask detection task.
- 500 images for the cigarette detection task.

The datasets provided the visual examples used in developing the respective detection models. The resulting model weights were exported in PyTorch format and integrated into the Python application.

The two trained model files are:

- "mask_model.pt"
- "cigarette.pt"

Using separate models allowed me to combine two object detection tasks without having to develop a single model covering both categories.

7. Application Features

The application includes the following functionality:

Live webcam detection

Captures video from the computer's default webcam and processes frames continuously.

Multiple object detection

Runs the face-mask and cigarette detection models on the same video frame.

Visual detection results

Displays model-generated bounding boxes and labels around detected objects.

Detection counts

Shows the number of detections returned by each model.

Image capture

Allows the user to save an annotated frame for later inspection.

Keyboard controls

- Press "C" to save the current processed frame.
- Press "Q" to close the application.

8. Application Screenshot

The screenshot below shows the application's visual interface.

"Computer Vision Application Screenshot" (./Screenshot%20(41).png)

9. Repository Structure

Computer-Vision-Project/
│
├── app.py
├── detector.py
├── camera.py
├── detector_xml.py
├── utils.py
│
├── mask_model.pt
├── cigarette.pt
├── yolov8n.pt
│
├── Screenshot (41).png
└── readme.md

Main Python Files

- "app.py": Main application entry point. Opens the webcam, reads video frames, calls the detection component and displays the processed output.
- "detector.py": Loads the two YOLOv8 models, performs object detection, combines the results and saves captured images.
- "camera.py": Contains a separate webcam utility for opening the camera, reading frames and releasing the camera resource. The main application currently handles webcam access directly.

The repository also contains the trained model weights and additional supporting Python files.

10. Installation and Running the Application

Requirements

- Python installed on your computer.
- A working webcam.
- An internet connection for installing the required Python packages.

Step 1: Clone the repository

git clone https://github.com/kennytoday/Computer-Vision-Project.git

Step 2: Open the project directory

cd Computer-Vision-Project

Step 3: Install dependencies

pip install ultralytics opencv-python

Step 4: Run the application

python app.py

The application should open the webcam and begin processing video frames.

Press "C" to save an image or "Q" to exit.

11. Testing and Observations

I tested the application using webcam input to observe how the two models performed when processing live video frames.

The testing helped me understand the importance of model quality, image conditions and the relationship between object detection and real-time video processing.

Some factors that can affect detection include:

- Lighting conditions and image quality.
- Distance between the camera and the object.
- Object visibility and positioning.
- Similar-looking objects in the background.
- The quality and variety of images used during model development.

The application demonstrates the integration of two object detection models into a working webcam-based system. However, I have not established a formal benchmark of its accuracy or real-world detection performance.

12. Limitations

Although the application provides a practical demonstration of object detection, there are limitations to consider.

The quality of detection depends on the training data and the conditions under which images are captured. Objects that are partially hidden, poorly illuminated or visually different from the training examples may not be recognised correctly.

The application also depends on the availability of a working webcam and sufficient computing resources to process video frames.

The system has not been developed or validated for clinical use, workplace enforcement or automated decision-making.

13. Future Development: IntelliVision AI

This project has contributed to my interest in developing more practical computer vision applications.

My longer-term vision is to explore IntelliVision AI, an idea focused on investigating how computer vision could support environmental safety and monitoring in healthcare settings.

Potential areas of exploration include identifying environmental hazards, supporting infection-prevention activities and providing visual information that may assist healthcare professionals.

This is a future development direction rather than an existing healthcare product. Any application in a clinical environment would require further development, appropriate testing, privacy safeguards and engagement with healthcare professionals.

14. What I Learned

Working on this project helped me develop a better understanding of how computer vision models can be integrated into practical applications.

In particular, I gained experience in:

- Working with YOLOv8 object detection models.
- Processing live video using OpenCV.
- Loading and integrating trained PyTorch model weights.
- Combining outputs from multiple detection models.
- Displaying bounding boxes, labels and detection counts.
- Handling webcam input and saving processed images.
- Recognising the limitations of model predictions in different environments.

It also strengthened my interest in applying AI and computer vision to practical challenges, particularly those connected to healthcare technology.

15. Disclaimer

This project is an independent technical development and learning exercise. Its detection results are experimental and should not be treated as definitive evidence of an individual's behaviour, infection status or compliance with safety requirements.

It is not a clinically validated or approved healthcare monitoring system.

Author

Kehinde Oni

GitHub: https://github.com/kennytoday

Project repository: https://github.com/kennytoday/Computer-Vision-Project