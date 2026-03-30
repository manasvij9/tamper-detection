# Visual Tampering & Anomaly Detection in Images

## 📌 Overview

This project focuses on detecting visual inconsistencies and potential tampering in digital images using fundamental Computer Vision techniques. Instead of relying on deep learning, the system leverages classical image processing and feature analysis methods to identify anomalies.

The goal is to analyze structural, frequency, and texture-based irregularities that may indicate image manipulation.

---

## Objectives

* Detect anomalies in images using Computer Vision techniques
* Analyze image consistency through edges, frequency, and texture
* Implement a lightweight and interpretable tampering detection pipeline
* Cover core concepts from Computer Vision syllabus

---

## Concepts Covered

This project demonstrates the application of:

### Module 1: Image Processing

* Gaussian Filtering
* Histogram Equalization
* Fourier Transform (Frequency Analysis)

### Module 3: Feature Extraction

* Edge Detection (Canny)
* Texture Analysis

### Module 4: Pattern Analysis

* Statistical Analysis (Variance)
* Rule-based Classification

---

## ⚙️ Tech Stack

* Python 3.x
* OpenCV
* NumPy
* Matplotlib

---

## 📁 Project Structure

tamper-detection/
│── data/                  # Input images
│── results/               # Output images and analysis
│── src/
│   ├── preprocessing.py
│   ├── analysis.py
│   ├── main.py
│── requirements.txt
│── README.md

---

## Setup Instructions

This project requires Python 3.7+ and relies on core computer vision libraries. It is designed to be run entirely from the command line without the need for a GUI or interactive notebooks.

### 1. Clone the Repository

Clone the project to your local machine:
```bash
git clone https://github.com/your-username/tamper-detection.git
cd tamper-detection
```

### 2. Set Up a Virtual Environment (Recommended)

It is highly recommended to use a virtual environment to isolate dependencies.
**On macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```
**On Windows:**
```bash
python -m venv venv
venv\\Scripts\\activate
```

### 3. Install Dependencies

Once the virtual environment is active, install the required packages:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Provide Input Data

The project operates on images placed in the `data/` directory. 
1. Create the `data/` directory if it does not exist: `mkdir data`
2. Place any test images (`.jpg`, `.jpeg`, `.png`) you wish to analyze inside the `data/` folder.

---

## ▶️ Execution (Command Line)

To run the tampering detection pipeline, execute the main script from the terminal:

```bash
python src/main.py
```

---

## 📊 Output

The system generates:

* Edge map of the image
* Frequency spectrum visualization
* Texture inconsistency analysis
* Final decision:

  * "Likely Authentic"
  * "Possible Tampering Detected"

Outputs are saved in the `results/` folder.

---

##  Methodology

1. **Preprocessing**

   * Image smoothing using Gaussian Blur
   * Contrast enhancement using histogram equalization

2. **Edge Analysis**

   * Detect structural inconsistencies using Canny edge detection

3. **Frequency Analysis**

   * Apply Fourier Transform to detect hidden anomalies

4. **Texture Analysis**

   * Analyze local variance across image patches

5. **Decision Logic**

   * Combine features to classify image consistency

---

##  Limitations

* Works best on visibly altered images
* Cannot detect highly sophisticated edits
* Depends on threshold-based heuristics

---

## Future Enhancements

* Integrate machine learning classifiers (KNN/SVM)
* Add localization of tampered regions
* Extend to video tampering detection

---

##  Author

Manasvi Joshi

---

## 📌 Notes

This project is implemented for academic purposes to demonstrate understanding of Computer Vision concepts and their practical applications.
