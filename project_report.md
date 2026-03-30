# Project Report: Visual Tampering & Anomaly Detection in Images

## 1. Abstract
With the proliferation of digital media, image manipulation and tampering have become increasingly common. This project implements a lightweight, fully interpretable computer vision pipeline designed to detect visual inconsistencies and potential image tampering. Rather than relying on opaque deep learning models, this system leverages foundational image processing, frequency analysis, and statistical techniques to identify structural and textural anomalies.

## 2. Problem Statement
The objective is to develop a command-line executable tool that can ingest an image and automatically evaluate it for signs of tampering (such as splicing, copy-move forgery, or localized retouching). The tool must be built using classical computer vision methods, ensuring the decision-making process is transparent and based on explicit mathematical and structural principles.

## 3. Syllabus Coverage & Methodology

The project successfully demonstrates the application of core Computer Vision concepts across multiple modules:

### Module 1: Image Processing
- **Gaussian Filtering**: Applied (`cv2.GaussianBlur`) to remove high-frequency noise that could cause false positives in edge detection.
- **Histogram Equalization**: Utilized (`cv2.equalizeHist`) to normalize contrast across the image, exposing faint or obscured details.
- **Fourier Transform (Frequency Analysis)**: Implemented (`np.fft.fft2`) to map the image into the frequency domain. Spliced or tampered regions often introduce out-of-band high frequencies or grid-like artifacts that stick out in the magnitude spectrum.

### Module 3: Feature Extraction
- **Edge Detection**: Employed the Canny edge detector (`cv2.Canny`) to highlight structural boundaries. Tampered images often present unnatural edge discontinuities or unusually high/low edge densities at the synthesis boundary.
- **Texture Analysis**: Computed local variance across patches using mathematical operations and mean filters. This helps identify regions that are unnaturally smooth (e.g., blurred to hide a splice) or unnaturally noisy.

### Module 4: Pattern Analysis
- **Rule-based Classification**: The system applies statistical thresholds (variance, frequency ratios, edge densities) to classify the image as "Likely Authentic" or "Possible Tampering Detected".

## 4. Implementation Details

### Architecture
The project is structured efficiently into distinct modules to maintain high code quality and separation of concerns:
- **`src/preprocessing.py`**: Handles I/O operations, noise reduction, and image enhancement.
- **`src/analysis.py`**: Contains the core mathematical computer vision operations (Canny, Fourier Transform, Variance maps).
- **`src/main.py`**: The orchestrator. It processes all images in the `data/` directory, extracts features, calculates heuristics, prints the final classification to standard output, and generates comprehensive visual mosaics.

### Execution Flow
1. **Load**: The image is read and converted to grayscale.
2. **Preprocess**: Gaussian smoothing followed by Histogram Equalization.
3. **Analyze**: Edge maps, frequency magnitude spectrum, and texture variance heatmaps are generated simultaneously.
4. **Evaluate**: Statistics (e.g., ratio of high-frequency pixels, max texture variance) are calculated.
5. **Classify**: Based on pre-defined heuristics, the system flags the image and prints specific reasons for anomalous behavior.
6. **Output**: Resulting feature maps are stitched into a `.png` mosaic and saved headlessly (without GUI popups) into the `results/` folder.

## 5. Results & Validation
During testing, the pipeline successfully identified structural discontinuities and high-frequency noise injection on dummy and manually spliced images. The terminal output cleanly outlines the specific factors contributing to the final decision. The tool proved it can execute in entirely headless environments, respecting the requirement for full CLI executability.

## 6. Limitations & Future Scope
- **Limitations**: The pipeline relies on hardcoded thresholds that may need calibration across dramatically different datasets (e.g., highly compressed JPEG vs. uncompressed PNG). It may struggle with highly sophisticated algorithms like GAN-generated deepfakes.
- **Future Enhancements**: Transitioning from threshold-based heuristics to a trained classifier (e.g., SVM or Random Forest) over the extracted features would improve robustness. Additionally, generating a bounding box mask around the anomalous regions would provide better explainability.

---
**Author**: Manasvi Joshi  
**Course Context**: Submitted for academic demonstration of fundamental Computer Vision techniques.
