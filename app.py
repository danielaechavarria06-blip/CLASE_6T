import streamlit as st
from PIL import Image

st.title("Dani mi primera app")
st.header("Dani estuvo aqui jeje")
st.write("Aplicación nadando")
image = Image.open('tiburoncito.png')
st.image(image, caption = "Tiburoncito u ja ja")


texto = st.text_input('Escribe el nombre de tu animal favorito', 'Mi animal fav')
st.write('El animal favorito del usuario es', texto)

st. subheader ("Ahora usemos 2 Columnas")
coll, col2 = st.columns(2)
with coll:
  st. subheader("Esta es la primera columna")
  st. write("Las interfaces multimodales mejoran la experiencia de usuario")
  resp = st. checkbox "Estoy de acuerdo')
  if resp:
    st.write('Correcto!')
