import streamlit as st 
from PIL import Image
st.title("Mi primera app ome")
st.header("Esto es un subtitulo")

image = Image.open("snoopy.png")
st.image(image, caption="snoopy.png")
