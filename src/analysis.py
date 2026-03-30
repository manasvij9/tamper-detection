import cv2
import numpy as np

def detect_edges(image, lower_thresh=100, upper_thresh=200):
    """Detects structural inconsistencies using Canny edge detection."""
    return cv2.Canny(image, lower_thresh, upper_thresh)

def frequency_analysis(image):
    """Applies Fourier Transform to detect frequency-based anomalies."""
    f_transform = np.fft.fft2(image)
    f_shift = np.fft.fftshift(f_transform)
    magnitude_spectrum = 20 * np.log(np.abs(f_shift) + 1)
    return magnitude_spectrum

def texture_analysis(image, window_size=5):
    """Analyzes local variance across image patches to detect texture anomalies."""
    # Compute local variance using mean filter
    # To avoid overflow, ensure we operate on floats
    img_float = image.astype(np.float32)
    mean_img = cv2.blur(img_float, (window_size, window_size))
    sq_mean_img = cv2.blur(img_float**2, (window_size, window_size))
    local_variance = sq_mean_img - mean_img**2
    return local_variance
