# BrainTumorCNN
Pollakrit Satasin 20/12/2021

A Convolutional Neural Network(CNN) that detects if there is a brain tumor (Glioma, Meningioma, Pituitary) from a CT scan image

## Usage
With downloading `main.py` and `BTCNN` folder, you can run the program in terminal with 
```bash
python main.py
```
then putting in your CT picture (.jpg), the program will output with the tumor prediction and the percentage of certainty.

## Training
The Convolutional Neural Network used in this project was written, compiled, and trained by Pollakrit Satasin on [Google Colaboratory](https://colab.research.google.com/)

The model architecture includes 11 layers as described

![](https://raw.githubusercontent.com/urseamajoris/BrainTumorCNN/blob/main/BTCNN/BTCNN_legend.png?raw=true)

The model was trained over 100 epochs with batch size of 112. The validation with 112 test images revealed  `92.78`% accuracy
