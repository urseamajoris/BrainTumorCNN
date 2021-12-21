import numpy as np
import tensorflow as tf
from tensorflow import keras
from BTCNN.postprocessing import posval

def loadmodel(data):
    model = keras.models.load_model('BTCNN\keras_pb')
    result = model.predict(data)
    return result