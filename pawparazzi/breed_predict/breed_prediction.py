import numpy as np
import tensorflow as tf

import cv2


def load_model():
    """
    Loads the model for breed prediction
    """
    model = tf.keras.models.load_model('models/model.keras') # type: ignore
    return model

def predict_breed(image, model):
    """
    Given an image return the prediction of the dog breed in given image
    """
    image = preprocess_image(image, 224)

    prediction = model.predict(image)

    score = tf.nn.softmax(prediction[0])
    best_id = np.argmax(score)
    return best_id

def preprocess_image(image, img_size):
    """
    Preprocessing function that takes in an image and sizes and normalizes it
    for the model
    """
    resized_img = cv2.resize(image, (img_size, img_size))
    resized_img = tf.expand_dims(resized_img, 0)
    return resized_img
