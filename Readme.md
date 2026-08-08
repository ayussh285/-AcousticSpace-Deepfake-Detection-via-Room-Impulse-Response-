# 🎙️ AcousticAI – Deepfake Audio Detection via Room Impulse Response (RIR)

## 📌 Project Overview

**AcousticAI** is an AI-powered Deepfake Audio Detection system that leverages **Room Impulse Response (RIR)** and acoustic features to distinguish between genuine and AI-generated speech. Unlike traditional approaches that rely solely on speech content, this project focuses on the environmental and acoustic fingerprints embedded within an audio recording, making it more robust against modern voice cloning and speech synthesis techniques.

The application follows a complete end-to-end pipeline—from audio upload and preprocessing to feature extraction, machine learning inference, and result visualization through an interactive web interface.

---

# 🎯 Objectives

- Detect AI-generated (Deepfake) audio using Room Impulse Response (RIR).
- Build a modular and scalable backend architecture.
- Preprocess audio recordings for high-quality feature extraction.
- Train machine learning models capable of classifying genuine and deepfake audio.
- Provide a simple and interactive web interface for real-time predictions.
- Visualize important audio characteristics for better interpretability.

---

# 🛠️ Tech Stack

## Programming Language
- Python

## Backend
- FastAPI

## Audio Processing
- Librosa
- NumPy
- SciPy
- SoundFile
- Noisereduce

## Machine Learning
- Scikit-learn
- TensorFlow / PyTorch
- Joblib

## Frontend
- Streamlit

## Version Control
- Git
- GitHub

---

# 📅 Weekly Development Progress

---

# ✅ Week 1 – Backend Development

## Objective

Design and develop the backend architecture that serves as the core processing engine of the application.

## Work Completed

- Designed a modular project structure for scalability and maintainability.
- Configured FastAPI as the backend framework.
- Developed REST APIs for handling audio uploads and processing requests.
- Created separate modules for preprocessing, feature extraction, inference, and utilities.
- Established routing mechanisms between frontend and backend.
- Configured project dependencies and development environment.
- Initialized Git repository and maintained version control throughout development.

## Outcome

By the end of Week 1, a fully functional backend infrastructure was established that efficiently accepts audio files and routes them through the complete processing pipeline.

---

# ✅ Week 2 – Audio Preprocessing & Feature Extraction

## Objective

Develop a reliable preprocessing pipeline capable of transforming raw audio into standardized inputs suitable for feature extraction and model training.

## Work Completed

### Audio Loading
- Implemented audio loading using Librosa.
- Standardized all recordings to a fixed sampling rate.
- Added support for multiple audio formats.

### Audio Validation
- Validated file formats.
- Checked recording duration constraints.
- Prevented corrupted or unsupported files from entering the pipeline.

### Audio Normalization
- Normalized signal amplitudes.
- Reduced recording volume inconsistencies.

### Silence Trimming
- Removed unnecessary leading and trailing silence.
- Improved processing efficiency.

### Noise Handling
- Explored and integrated noise reduction techniques.
- Produced cleaner audio signals for downstream processing.

### Feature Preparation

Prepared the preprocessing pipeline for extracting important acoustic features including:

- Room Impulse Response (RIR)
- MFCC
- Mel Spectrogram
- Chroma Features
- Spectral Contrast
- Additional acoustic descriptors

## Outcome

A reusable preprocessing pipeline was successfully developed that consistently prepares audio recordings for feature extraction and machine learning.

---

# ✅ Week 3 – Model Training & Setup

## Objective

Develop and train the machine learning model capable of accurately distinguishing genuine and AI-generated audio samples.

## Work Completed

### Dataset Preparation
- Organized genuine and deepfake audio datasets.
- Balanced the dataset for fair model learning.
- Split the dataset into training, validation, and testing sets.

### Feature Extraction
- Generated feature vectors from preprocessed audio.
- Stored extracted features for efficient model training.

### Model Development
- Trained machine learning models on extracted acoustic features.
- Experimented with multiple classification algorithms.
- Tuned hyperparameters to improve prediction performance.

### Model Evaluation
- Evaluated model performance using accuracy.
- Generated confusion matrix.
- Calculated precision, recall, and F1-score.
- Compared model performance across experiments.

### Model Saving
- Saved the trained model using Joblib.
- Prepared the model for deployment and inference.

## Outcome

By the end of Week 3, a trained deepfake detection model capable of classifying genuine and AI-generated audio using acoustic features was successfully integrated into the project pipeline.

---

# ✅ Week 4 – Frontend Development

## Objective

Develop a user-friendly interface that enables users to upload audio recordings and receive deepfake detection results in real time.

## Work Completed

### User Interface
- Developed an interactive frontend using Streamlit.
- Designed a clean and responsive interface.
- Implemented drag-and-drop audio upload functionality.

### Backend Integration
- Connected the frontend with FastAPI backend APIs.
- Enabled seamless communication between frontend and backend modules.
- Displayed processing status throughout the inference pipeline.

### Prediction Interface
- Integrated the trained machine learning model.
- Displayed prediction labels (Genuine / Deepfake).
- Presented confidence scores for each prediction.

### Audio Visualization
- Displayed uploaded audio information.
- Visualized waveforms and spectrograms.
- Showed extracted acoustic features for better interpretability.

### User Experience
- Added loading indicators.
- Implemented robust input validation.
- Improved responsiveness and overall usability.
- Provided meaningful error handling for invalid inputs.

## Outcome

By the end of Week 4, a complete end-to-end application was successfully developed. Users can upload an audio recording through the Streamlit interface, which communicates with the FastAPI backend, performs preprocessing and feature extraction, executes the trained deepfake detection model, and displays prediction results along with relevant visualizations in real time.

---

# 🔄 Project Workflow

```text
                User Uploads Audio
                        │
                        ▼
            Streamlit Frontend Interface
                        │
                        ▼
               FastAPI Backend API
                        │
                        ▼
               Audio Validation Module
                        │
                        ▼
            Audio Preprocessing Pipeline
                        │
                        ▼
      Acoustic Feature Extraction (RIR,
   MFCC, Mel Spectrogram, Chroma, etc.)
                        │
                        ▼
         Trained Deepfake Detection Model
                        │
                        ▼
          Genuine / Deepfake Prediction
                        │
                        ▼
      Results, Confidence & Visualizations
```

---

# 📈 Current Progress

| Module | Status |
|---------|--------|
| Backend Development | ✅ Completed |
| Audio Preprocessing | ✅ Completed |
| Feature Extraction Pipeline | ✅ Completed |
| Dataset Preparation | ✅ Completed |
| Model Training | ✅ Completed |
| Model Evaluation | ✅ Completed |
| Streamlit Frontend | ✅ Completed |
| FastAPI Integration | ✅ Completed |
| End-to-End Pipeline | ✅ Completed |
| Deployment | ⏳ Future Enhancement |

---

# 🚀 Future Enhancements

- Improve Room Impulse Response estimation techniques.
- Support multiple benchmark deepfake audio datasets.
- Add batch audio prediction functionality.
- Deploy the application on cloud platforms.
- Optimize inference speed for real-time performance.
- Explore advanced deep learning architectures for higher accuracy.
- Enhance visualization and reporting capabilities.
- Develop a REST API for third-party integration.

---

# 👥 Contributors

Developed as part of the **AcousticAI – Deepfake Audio Detection via Room Impulse Response (RIR)** project.

---