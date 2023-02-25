import urllib.request
import io
import numpy as np
import tensorflow as tf
import cv2
from tensorflow.keras.preprocessing.image import img_to_array, load_img

# Load the trained DeepGlobe model
model = tf.keras.models.load_model('path_to_model.h5')

# Function to predict the geolocation of an image
def predict_location(image_path):
    if image_path.startswith("http"):
        req = urllib.request.urlopen(image_path)
        arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
        img = cv2.imdecode(arr, -1)
    else:
        img = cv2.imread(image_path)

    # Preprocess the image
    img = cv2.resize(img, (224, 224))
    img = img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = tf.keras.applications.resnet50.preprocess_input(img)

    # Make the prediction
    prediction = model.predict(img)

    # Get the predicted coordinates
    lon, lat = prediction[0]

    # Generate a map URL with the predicted location
    map_url = f'https://www.openstreetmap.org/?mlat={lat}&mlon={lon}#map=16/{lat}/{lon}'

    return map_url


# Print the result
print(f"The predicted location of the image is: {map_url}")
