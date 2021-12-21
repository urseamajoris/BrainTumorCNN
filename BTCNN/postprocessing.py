import numpy as np
import math

def posval(predictions):
    
    predlist = predictions.tolist()
    
    c100 = max(predlist)
    certainty = max(c100)
    
    pos = c100.index(certainty)
    certainty = certainty * 100
    ctr_rounded = int(certainty)
    
    ref = {0:'no tumor', 1:'glioma', 2:'meningioma', 3:'pituitary'}
    print(f'prediction found :{ref[pos]}, with {ctr_rounded}% certainty')

