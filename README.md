# LSH-based Audio Duplicate Detection with MFCC Features

This project is an implementation of audio duplicate detection using Locality-Sensitive Hashing (LSH) and Mel Frequency Cepstral Coefficients (MFCC) features. The application is built using Flask for the backend and HTML/CSS for the frontend.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Dependencies](#dependencies)

## Overview

The purpose of this project is to identify duplicate audio files by extracting MFCC features from audio data and using LSH for efficient similarity search. The application provides a user-friendly web interface for uploading and comparing audio files.

## Features

- **Audio Upload**: Upload audio files through the web interface.
- **Feature Extraction**: Extract MFCC features from the uploaded audio files.
- **Duplicate Detection**: Use LSH to detect and identify duplicate audio files.
- **Results Display**: Display results on the web interface indicating potential duplicates.

## Installation on Windows

1. Clone the repository:
    ```sh
    git clone https://github.com/UmmeHani-DS/LSH-based-Audio-Duplicate-Detection-with-MFCC-Features.git
    cd LSH-based-Audio-Duplicate-Detection-with-MFCC-Features
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    venv\Scripts\activate
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up Flask environment variables:
    ```sh
    set FLASK_APP=app.py
    set FLASK_ENV=development  # For development mode
    ```

5. Run the Flask application:
    ```sh
    flask run
    ```

6. Open your browser and navigate to `http://127.0.0.1:5000` to use the application.

## Usage

1. Open the web application in your browser.
2. Upload one or more audio files using the provided interface.
3. Click on the "Detect Duplicates" button.
4. View the results displaying potential duplicate audio files.

## How It Works

1. **Audio Upload**: Users upload audio files through the web interface.
2. **MFCC Extraction**: The backend extracts MFCC features from the uploaded audio files. MFCCs are a representation of the short-term power spectrum of sound, commonly used in audio processing.
3. **LSH Indexing**: The extracted MFCC features are hashed into an LSH index. LSH is used to reduce the dimensionality of the feature space and to enable efficient similarity searches.
4. **Duplicate Detection**: The system compares the LSH hashes to identify similar (duplicate) audio files.
5. **Results Display**: The results, indicating which audio files are potential duplicates, are displayed on the web interface.

## Dependencies

- Flask
- NumPy
- SciPy
- librosa
- scikit-learn
- HTML/CSS for the frontend

Install all dependencies using:
```sh
pip install -r requirements.txt
