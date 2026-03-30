import cv2
import numpy as np

def load_image(image_path):
    """Loads an image in grayscale and color."""
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Could not load image at {image_path}")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return image, gray

def apply_gaussian_blur(image, kernel_size=(5, 5)):
    """Applies Gaussian Blur for noise reduction."""
    return cv2.GaussianBlur(image, kernel_size, 0)

def enhance_contrast(image):
    """Enhances contrast using Histogram Equalization."""
    return cv2.equalizeHist(image)
