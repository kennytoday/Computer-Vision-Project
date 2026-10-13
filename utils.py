"""
utils.py
-----------------------
Utility functions for the Computer Vision project.
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

    return cv2.resize(
        frame,
        (width, height)
    )


# ===========================================
# Convert to Gray
# ===========================================

def gray(frame):

    return cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )


# ===========================================
# Draw FPS
# ===========================================

def draw_fps(frame, fps):

    draw_text(
        frame,
        f"FPS: {fps:.2f}",
        (10, 60),
        (255, 255, 0)
    )