# Brain Tumor Detection using CNN

This project implements a Convolutional Neural Network (CNN) using Keras with a TensorFlow backend to detect the presence of brain tumors in MRI scan images. It includes scripts for training the model and a simple web application built with Flask to perform predictions on uploaded images.

## Table of Contents
- [Features](#features)
- [Dataset](#dataset)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [How to Run](#how-to-run)
- [File Structure](#file-structure)

## Features

- Image preprocessing for the model.
- A CNN model built and trained using Keras.
- A web interface built with Flask to upload an MRI image and get a prediction.

## Dataset

The model is trained on a dataset of MRI images. For the training script (`MainTrain.py`) to work correctly, the images must be organized into two folders within the `datasets` directory:

- `datasets/yes/`: Contains MRI images with brain tumors.
- `datasets/no/`: Contains MRI images without brain tumors.

## Technologies Used

- Python 3
- TensorFlow & Keras
- Flask
- OpenCV
- Pillow (PIL)
- NumPy
- Scikit-learn

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-link>
    cd BrainTumorDetection_main
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    Install the required packages using the `requirements.txt` file.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Create `uploads` directory:**
    The Flask application saves uploaded files to an `uploads` directory, which you need to create.
    ```bash
    mkdir uploads
    ```

## How to Run

1.  **Train the Model:**
    - Run the `MainTrain.py` script to train the model on the images in the `datasets` folder.
    ```bash
    python MainTrain.py
    ```
    - This will save the trained model as `BrainTumor10EpochsCategorical.h5`. Note that `app.py` currently expects `BrainTumor10Epochs.h5`. You may need to rename the saved model or update the filename in `app.py`.

2.  **Run the Web Application:**
    - Start the Flask server.
    ```bash
    python app.py
    ```
    - Open your web browser and go to `http://127.0.0.1:5000/`.
    - Upload an MRI image to see the prediction.

## File Structure

```
BrainTumorDetection_main/
├── app.py                  # Main Flask application file
├── MainTrain.py            # Script for training the CNN model
├── requirements.txt        # Project dependencies
├── Test.py                 # Script for testing the model on a single image
├── BrainTumor10Epochs.h5   # The trained model file
├── datasets/
│   ├── no/                 # Images without tumors
│   └── yes/                # Images with tumors
├── templates/
│   └── index.html          # Frontend for the web app
└── uploads/                # Folder for user-uploaded images
```