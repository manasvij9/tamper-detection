import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from preprocessing import load_image, apply_gaussian_blur, enhance_contrast
from analysis import detect_edges, frequency_analysis, texture_analysis

def analyze_image(image_path, output_dir):
    """Runs the tamper detection pipeline on a given image."""
    print(f"\\n[{'-'*40}]")
    print(f"Analyzing {os.path.basename(image_path)}...")
    print(f"[{'-'*40}]")
    try:
        color_img, gray_img = load_image(image_path)
    except Exception as e:
        print(f"Error loading image: {e}")
        return
        
    os.makedirs(output_dir, exist_ok=True)
    basename = os.path.basename(image_path).split('.')[0]
    
    # Preprocessing
    smoothed = apply_gaussian_blur(gray_img)
    enhanced = enhance_contrast(smoothed)
    
    # Analysis
    edges = detect_edges(enhanced)
    freq_spectrum = frequency_analysis(enhanced)
    texture_var = texture_analysis(enhanced)
    
    # Decision Logic (Rule-based heuristics)
    # 1. Edge Density Anomaly (Unusually high or low edges)
    edge_density = np.sum(edges > 0) / (edges.shape[0] * edges.shape[1])
    
    # 2. Texture Variance Anomaly (Suspicious patches of low/high variance)
    avg_variance = np.mean(texture_var)
    max_variance = np.max(texture_var)
    
    # 3. Frequency domain checks (High frequency artifacts)
    # Mean and standard dev. To detect anomalous high energy.
    mean_freq = np.mean(freq_spectrum)
    std_freq = np.std(freq_spectrum)
    high_freq_ratio = np.sum(freq_spectrum > (mean_freq + 2*std_freq)) / freq_spectrum.size
    
    print(f"Edge Density:           {edge_density:.4f}")
    print(f"Average Texture Variance: {avg_variance:.2f}")
    print(f"Max Texture Variance:   {max_variance:.2f}")
    print(f"High Frequency Ratio:   {high_freq_ratio:.4f}")
    
    is_tampered = False
    reasons = []
    
    # Note: These thresholds are experimental heuristics and may need tuning based on images
    if edge_density > 0.15 or edge_density < 0.005:
        is_tampered = True
        reasons.append("Anomalous edge density detected (structure inconsistency).")
        
    if max_variance > 10000: # Threshold for unnatural texture variance
        is_tampered = True
        reasons.append("Unnaturally high local variance detected (potential cloning/splicing).")
        
    if high_freq_ratio > 0.05:
        is_tampered = True
        reasons.append("High ratio of out-of-band high frequencies detected in Fourier Transform.")
        
    decision = "Possible Tampering Detected" if is_tampered else "Likely Authentic"
    print(f"\\n>>> Final Decision: {decision} <<<")
    if reasons:
        for r in reasons:
            print(f"- {r}")

    # Plot and save results
    plt.figure(figsize=(15, 10))
    
    plt.subplot(231)
    plt.imshow(cv2.cvtColor(color_img, cv2.COLOR_BGR2RGB))
    plt.title('Original Image')
    plt.axis('off')
    
    plt.subplot(232)
    plt.imshow(enhanced, cmap='gray')
    plt.title('Enhanced Grayscale')
    plt.axis('off')
    
    plt.subplot(233)
    plt.imshow(edges, cmap='gray')
    plt.title('Edge Detection (Canny)')
    plt.axis('off')
    
    plt.subplot(234)
    plt.imshow(freq_spectrum, cmap='gray')
    plt.title('Frequency Spectrum (Magnitude)')
    plt.axis('off')
    
    plt.subplot(235)
    plt.imshow(texture_var, cmap='hot')
    plt.title('Texture Local Variance')
    plt.axis('off')
    
    plt.tight_layout()
    output_path = os.path.join(output_dir, f"{basename}_analysis.png")
    plt.savefig(output_path)
    print(f"\\n> Saved analysis visualization to {output_path}")
    plt.close()

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(current_dir, "..", "data")
    output_dir = os.path.join(current_dir, "..", "results")
    
    # Process all images in data_dir
    os.makedirs(data_dir, exist_ok=True)
    images = [f for f in os.listdir(data_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    if not images:
        print(f"No images found in {os.path.abspath(data_dir)}.\\nPlease place some test images in the data/ directory and run again.")
    else:
        for img_name in images:
            analyze_image(os.path.join(data_dir, img_name), output_dir)
