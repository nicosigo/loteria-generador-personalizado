
import random
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Generador Estratégico de Números para Lotería", layout="centered")
st.title("🎯 Generador Estratégico de Números para Lotería – Modo Intención")

with st.expander("ℹ️ ¿Cómo funciona esta app?"):
    st.markdown("""
### 🎯 ¿Cómo funciona esta aplicación?

Bienvenido al **Generador Estratégico de Números para Lotería – Modo Intención**. Esta app combina psicología, numerología y estadística para crear combinaciones estratégicas de números según tu intención emocional y estratégica.
""")

def generar_combinacion(cantidad_total):
    return sorted(random.sample(range(1, 70), cantidad_total))

def mostrar_animacion(jugada):
    bolas_html = "".join([f"<span>{num}</span>" for num in jugada])
    components.html(bolas_html)

cantidad_numeros = st.slider("Cantidad de números:", 2, 10, 6)
cantidad_jugadas = st.slider("Cantidad de jugadas:", 1, 5, 3)

if st.button("Generar combinaciones"):
    for i in range(cantidad_jugadas):
        jugada = generar_combinacion(cantidad_numeros)
        mostrar_animacion(jugada)
