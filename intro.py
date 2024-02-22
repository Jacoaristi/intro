import streamlit as st
from PIL import Image

st.title("Mi primera App!!")
st.header("Este es el espacio para desarrollar las aplicaciones que considere de mi agrado para interfaces multimodales")
st.write("facilmente puedo realizar backend y frontend")
image= Image.open("1.png")

st.image(image, caption='art peter giffin')

texto = st.text_input('Escribe algo', 'Este es mi texto')
