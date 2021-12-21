import os
from PIL import Image, ImageOps
import numpy as np
from tensorflow.keras import backend as K

def open(PATH):
    img = Image.open(PATH)
    img = img.resize([64,64])
    img = ImageOps.grayscale(img)
    img = np.array(img)
    img = img/255
    img = img.astype('float32')
    img = img/255
    img = img.reshape([1, 64, 64, 1])
    
    
    return img
