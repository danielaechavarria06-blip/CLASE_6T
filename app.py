import streamlit as st
from PIL import Image

# ------------------------
# TÍTULOS
# ------------------------
st.title("Dani mi primera app")
st.header("Dani estuvo aqui jeje")
st.write("Aplicación nadando")

# ------------------------
# IMAGEN
# ------------------------
image = Image.open('tiburoncito.png')
st.image(image, caption="Tiburoncito u ja ja")

# ------------------------
# INPUT DE TEXTO
# ------------------------
texto = st.text_input(
    'Escribe el nombre de tu animal favorito',
    'Mi animal fav'
)
st.write('El animal favorito del usuario es:', texto)

# ------------------------
# COLUMNAS
# ------------------------
st.subheader("Ahora usemos 2 Columnas")
col1, col2 = st.columns(2)

# -------- Columna 1 --------
with col1:
    st.subheader("Esta es la primera columna")
    st.write("Las interfaces multimodales mejoran la experiencia de usuario")

    resp = st.checkbox("Estoy de acuerdo")

    if resp:
        st.success("¡Correcto!")

# -------- Columna 2 --------
with col2:
    st.subheader("Esta es la segunda columna")

    modo = st.radio(
        "¿Qué modalidad es la principal en tu interfaz?",
        ("Visual", "Auditiva", "Táctil")
    )

    if modo == "Visual":
        st.info("La vista es fundamental para tu interfaz")

    elif modo == "Auditiva":
        st.info("La audición es fundamental para tu interfaz")

    elif modo == "Táctil":
        st.info("El tacto es fundamental para tu interfaz")
