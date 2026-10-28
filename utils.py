"""
utils.py
-----------------------
Utility functions for the Computer Vision project.

These are small helper functions you can reuse.
They make it easier to draw text, draw boxes,
save pictures, resize images, etc.
Right now the main detector.py does some of this itself,
but these functions are nice if you want to clean the code up later.
"""

import cv2
import os
from datetime import datetime


# ===========================================
# Draw Text
# ===========================================

def draw_text(frame,
              text,
              position=(10, 30),
              color=(0, 255, 0),
              scale=0.8,
              thickness=2):
    """
    Write text on an image.
    Example: draw_text(frame, "Hello", (10, 30))
    """
    cv2.putText(
        frame,
        text,
        position,
        cv2.FONT_HERSHEY_SIMPLEX,
        scale,
        color,
        thickness
    )


# ===========================================
# Draw Rectangle
# ===========================================

def draw_box(frame,
             x,
             y,
             w,
             h,
             color=(0, 255, 0),
             thickness=2):
    """
    Draw a rectangle (box) on an image.
    x, y = top-left corner
    w, h = width and height of the box
    """
    cv2.rectangle(
        frame,
        (x, y),
        (x + w, y + h),
        color,
        thickness
    )


# ===========================================
# Save Image
# ===========================================

def save_image(frame):
    """
    Save a frame as a .jpg file in the "captures" folder.
    The filename is based on the current date and time.
    """
    # Create the folder if it doesn't exist
    os.makedirs("captures", exist_ok=True)

    filename = datetime.now().strftime(
        "captures/%Y%m%d_%H%M%S.jpg"
    )

    cv2.imwrite(filename, frame)

    return filename


# ===========================================
# Resize Image
# ===========================================

def resize(frame, width=640, height=480):
    """
    Change the size of an image.
    Useful if the camera is giving you a very large picture
    and you want something smaller and faster.
    """
    return cv2.resize(
        frame,
        (width, height)
    )


# ===========================================
# Convert to Gray
# ===========================================

def gray(frame):
    """
    Turn a color image into black-and-white (grayscale).
    Many computer vision tasks work better on gray images.
    """
    return cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )


# ===========================================
# Draw FPS
# ===========================================

def draw_fps(frame, fps):
    """
    Show the frames-per-second (how fast the video is running)
    on the image. Higher FPS = smoother video.
    """
    draw_text(
        frame,
        f"FPS: {fps:.2f}",
        (10, 60),
        (255, 255, 0)   # yellow color
    )
