from flask import Flask, render_template, request
from keras.models import load_model
from PIL import Image
import numpy as np


app = Flask(__name__)

dic = {0 : 'NORMAL', 1 : 'PNUEMONIA'}

model = load_model('model.h5', compile=False)

model.make_predict_function()

def predict_label(img_path):
    img = Image.open(img_path)
    img = img.resize((1000, 1000))  # Resize the image to match the model's expected input size
    img_array = np.asarray(img) / 255.0

    # Ensure the shape matches the expected input shape
    img_array = img_array.reshape(1, 1000, 1000, 3)  # Reshape according to the model's input shape
    prediction = model.predict(img_array)
    predicted_class = np.argmax(prediction, axis=1)[0]
    return dic[predicted_class]




# routes
@app.route("/", methods=['GET'])
def main():
	return render_template("main.html")

@app.route("/classification", methods=['GET', 'POST'])
def classification():
	return render_template("classification.html")

@app.route("/submit", methods = ['GET', 'POST'])
def get_output():
	if request.method == 'POST':
		img = request.files['my_image']

		img_path = "static/" + img.filename
		img.save(img_path)

		p = predict_label(img_path)

	return render_template("classification.html", prediction = p, img_path = img_path)


if __name__ =='__main__':
	#app.debug = True
	app.run(debug = True)
