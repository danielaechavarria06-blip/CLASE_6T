import streamlit as st
from PIL import Image

st.title("Dani mi primera app")
st.header("Dani estuvo aqui jeje")
st.write("Aplicación nadando")
image = Image.open('tiburoncito.png')
st.image(image, caption = "Tiburoncito u ja ja")


texto = st.text_input('Escribe el nombre de tu animal favorito', 'Mi animal fav')
st.write('El animal favorito del usuario es', texto)
