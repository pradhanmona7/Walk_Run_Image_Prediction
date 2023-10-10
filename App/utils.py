import os
import numpy as np
from PIL import Image
import tensorflow
from tensorflow import keras
from tensorflow.keras.preprocessing import image

# Force Tesorflow to use CPU
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

model = keras.models.load_model("./model_05-0.94.h5")

def predict(img):
    # Load the Image
    img = Image.open(img).convert('RGB')

    # Resize Image to size of (300, 300)
    img = tensorflow.image.resize(img, (300, 300))

    # Convert Image to a numpy array
    img = image.img_to_array(img, dtype=np.uint8)

    # Scaling the Image Array values between 0 and 1
    img = np.array(img)/255.0

    # Get the Predicted Label for the loaded Image
    prediction = model.predict(img[np.newaxis, ...])

    # Label array
    labels = {0: 'run', 1: 'walk'}

    # Predicted Class
    predicted_class = labels[np.argmax(prediction[0], axis=-1)]

    return [prediction, predicted_class]