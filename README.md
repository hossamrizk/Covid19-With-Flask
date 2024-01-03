# COVID-19 X-ray Image Classifier

## Overview
This project aims to classify X-ray images of COVID-19 patients into two categories: 'Normal' or 'Pneumonia'. The classifier is based on a Convolutional Neural Network (CNN) model trained on a dataset of X-ray images.

## Features
- Classification of X-ray images into 'Normal' or 'Pneumonia'.
- Built using Flask and Streamlit to provide an API for inference and a user-friendly interface.

## Setup and Usage
### Installation
1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/Covid19-With-Flask-And-STREAMLIT.git
    cd Covid19-With-Flask-And-STREAMLIT
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Running the Application
- To start the Flask API:

    ```bash
    python app.py
    ```

- To launch the Streamlit interface:

    ```bash
    streamlit run api.py
    ```

### Usage
- Visit the Streamlit app (`localhost:8501`) to interactively test the classifier.
- Use the Flask API (`localhost:5000`) to make predictions programmatically.

## Model Training
- The CNN model is trained on a dataset of COVID-19 X-ray images.
- Training details and model architecture can be found in the [(https://www.kaggle.com/code/hossamrizk/your-first-step-in-cnn)https://www.kaggle.com/code/hossamrizk/your-first-step-in-cnn notebook.](https://www.kaggle.com/code/hossamrizk/your-first-step-in-cnn)https://www.kaggle.com/code/hossamrizk/your-first-step-in-cnn

