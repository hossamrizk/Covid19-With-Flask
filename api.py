import streamlit as st
from PIL import Image
from keras.models import load_model
import numpy as np

model = load_model('model.h5', compile=False)

def main():
    st.title('COVID-19 Chest Image Classification')

    # Image upload option
    uploaded_image = st.file_uploader("Upload Chest X-ray Image", type=["jpg", "jpeg", "png"])

    # Prediction button
    if uploaded_image is not None:
        # Display the uploaded image
        image = Image.open(uploaded_image)
        st.image(image, caption='Uploaded Chest X-ray', use_column_width=True)

        # Preprocess the image for the model
        image = np.array(image.resize((1000,1000)))  # Resize the image according to your model's input size
        image = image / 255.0  # Normalize the pixel values
        image = np.expand_dims(image, axis=0)  # Add batch dimension

        # Make the prediction
        prediction = model.predict(image)
        predicted_class = np.argmax(prediction, axis=1)[0]

        # Define the classes for COVID-19 classification
        classes = ['Normal', 'Pneumonia']  # Modify based on your model's output classes

        st.write(f'Predicted Class: {classes[predicted_class]}')

if __name__ == '__main__':
    main()