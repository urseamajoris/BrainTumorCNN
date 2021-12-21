from pathlib import Path
from numpy import load
from BTCNN.predictions import loadmodel
from BTCNN.preprocessing import open
from BTCNN.postprocessing import posval
import tensorflow as tf


def greet():
    print('type image file name:')
    name = input()
    return name

def script():
    PATH = greet()
    img = open(PATH)
    x = loadmodel(img)
    output = posval(x)

    return output


