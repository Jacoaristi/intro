import streamlit as st
from PIL import Image

st.title("Mi primera App!!")
st.header("Este es el espacio para desarrollar las aplicaciones que considere de mi agrado para interfaces multimodales")
st.write("facilmente puedo realizar backend y frontend")
image= Image.open("1.png")

st.image(image, caption='art peter giffin')

texto = st.text_input('Escribe algo', 'Este es mi texto')
st.write('El texto escrito es', texto)

st.subheader("Ahora usemos 2 Comlumnas")
col1, col2 = st.columns(2)

with col1: 
  st.subheader ("Esta es la primera columna")
  st.write("Las interfaces multimodales mejoran la experiencia de usuario")
  resp = st.checkbox('Estoy de acuerdo')
  if resp:
    st. write ('Correcto!')

with col2: 
  st.subheader ("Esta es la segunda columna")
  modo = st.radio ("Que modalidad es la principal en tu interfaz",('Visual','auditiva','Táctil' ))
  if modo == 'Visual':
   st.write ('La vista es fundamental para tu interfaz')
  if modo == 'auditiva':
   st.write ('La audicion es fundamental para tu interfaz')
  if modo == 'Táctil':
   st.write ('El tacto es fundamental para tu interfaz')
