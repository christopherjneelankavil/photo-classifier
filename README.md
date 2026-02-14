# Photo Classifier

A hybrid AI and Computer Vision project that automatically downloads a dataset of images and sorts them into specific categories like "Eyes Closed", "Blurry", "Group Photos", and "Animals".

**🔗 GitHub Repository:** [https://github.com/christopherjneelankavil/photo-classifier](https://github.com/christopherjneelankavil/photo-classifier)

## 📌 Overview

This tool uses a combination of deep learning (MobileNetV2, MediaPipe) and classical computer vision (OpenCV) to classify images without needing to train a model from scratch. It is designed to be lightweight and run on a standard CPU.

## 🚀 How It Works

The project consists of two main scripts:

1.  **Data Collection (`download_dataset.py`)**: Fetches sample images from LoremFlickr based on keywords (e.g., "smile", "dog", "blur").
2.  **Photo Sorting (`photo_sorter.py`)**: Analyzes the images and sorts them into folders in `output/` based on their content:
    -   **Face Detection**: Uses MediaPipe to count faces (Solo vs. Group vs. No Human).
    -   **Blur Detection**: Uses OpenCV Laplacian variance to detect blurry images.
    -   **Smile & Eye Detection**: Uses OpenCV Haar Cascades.
    -   **Object/Animal Detection**: Uses MobileNetV2 (ImageNet) to identify animals.

For a detailed explanation of the algorithms and design choices, please read the **[Photo Classification Report](photo_classification_report.md)**.

## 🛠️ Setup & Installation

> [!IMPORTANT]
> **Python 3.10 is required.** Some dependencies (like MediaPipe) may not support newer Python versions on all platforms.

### Step 1: Clone the Repository
```bash
git clone https://github.com/christopherjneelankavil/photo-classifier.git
cd photo-classifier
```

### Step 2: Create a Virtual Environment

It is recommended to use **Conda** or `venv` to avoid conflicts. Since this project requires **Python 3.10**, Conda is the easiest way to manage this.

#### Option A: Using Conda (Recommended)
```bash
conda create -n photo-classifier python=3.10
conda activate photo-classifier
```

#### Option B: Using venv (Standard Python)
If you already have Python 3.10 installed:
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
With your virtual environment activated, install the required packages:
```bash
pip install -r requirements.txt
```
*Note: This project requires `tensorflow`, `mediapipe`, `opencv-contrib-python`, and `numpy`.*

## 💻 How to Run

### Step 1: Download the Dataset
Run the downloader script to fetch test images:
```bash
python download_dataset.py
```
This will create a `dataset/` folder and download roughly 35 random images across different categories.

### Step 2: Sort the Photos
Run the sorter script to classify the images:
```bash
python photo_sorter.py
```
This will process images from `dataset/` and organize them into the `output/` folder.

### Step 3: Check Results
Navigate to the `output/` directory to see your sorted images:
-   📂 `output/Animals`
-   📂 `output/Blurry`
-   📂 `output/Eyes_Closed`
-   📂 `output/Group`
-   📂 `output/No_Human`
-   📂 `output/Smiled`
-   📂 `output/Solo`

## 📁 Project Structure

```
D:\PhotoClassifier\
│
├── download_dataset.py           # Script to download sample images
├── photo_sorter.py               # Main logic for classifying and sorting images
├── photo_classification_report.md # Detailed report on the approach and models
├── requirements.txt              # List of python dependencies
├── dataset/                      # (Created at runtime) Raw downloaded images
└── output/                       # (Created at runtime) Sorted image folders
```

## 📖 Classification Report

I have included a detailed report explaining why this specific hybrid approach was chosen over training a single massive model. It covers:
-   Why we combine MediaPipe, OpenCV, and MobileNetV2.
-   The limitations of each method.
-   Why this is efficient for small datasets on a laptop.

👉 **Read the full report here:** [photo_classification_report.md](photo_classification_report.md)
