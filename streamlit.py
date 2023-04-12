import streamlit as st

from src.set_background import set_background
from PIL import Image
import numpy as np
import cv2
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions


st.markdown('<h1 style="color:black;">Modelo de Classificação de Imagens ResNet50</h1>', unsafe_allow_html=True)
st.markdown('<h4 style="color:black;">Por: Bruno Caraffa</h4>', unsafe_allow_html=True)

set_background('content/bg.webp')

upload= st.file_uploader("Carregue imagem para classificação", type=['png','jpg'])
c1, c2= st.columns(2)

if upload is not None:
    img = Image.open(upload)
    x_raw = np.asarray(img)
    x_raw = cv2.resize(x_raw,(224, 224))
    x = np.array([x_raw])
    x = preprocess_input(x)
    c1.header(':violet[Imagem]')
    c1.image(img)

    model = ResNet50(weights="imagenet")
    preds = model.predict(x)
    predictions = decode_predictions(preds, top=3)[0]
    c2.header('Top 3 Previsões')
    c2.write(predictions[0][1:])
    c2.write(predictions[1][1:])
    c2.write(predictions[2][1:])
    


