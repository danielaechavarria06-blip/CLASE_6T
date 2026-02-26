import streamlit as st
from PIL import Image

st.title("Dani mi primera app")
st.header("Dani estuvo aqui jeje")
st.write("Aplicación nadando")

# Cargar imagen
image = Image.open('tiburoncito.png')
st.image(image, caption="Tiburoncito u ja ja")

# Input de texto
texto = st.text_input('Escribe el nombre de tu animal favorito', 'Mi animal fav')
st.write('El animal favorito del usuario es', texto)

# Columnas
st.subheader("Ahora usemos 2 Columnas")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Esta es la primera columna")
    st.write("Las interfaces multimodales mejoran la experiencia de usuario")
    resp = st.checkbox("Estoy de acuerdo")
    
    if resp:
        st.write("¡Correcto!")

with col2:
    st.subheader("Esta es la segunda columna")
    st.write("Aquí puedes agregar más contenido")
