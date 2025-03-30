
import random
import time
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Generador de Números para Lotería", layout="centered")

st.title("🎲 Generador Estratégico de Números para Lotería")
st.markdown("Este generador combina lógica simbólica, estadística y estrategia psicológica para ayudarte a elegir tus números de forma más consciente.")

base_numbers = [7, 13, 22, 33, 41, 69]

def generar_combinacion(cantidad_total):
    proporcion_fechas = 0.35
    proporcion_altos = 0.35
    proporcion_simbolicos = 0.3

    cantidad_fechas = round(cantidad_total * proporcion_fechas)
    cantidad_altos = round(cantidad_total * proporcion_altos)
    cantidad_simbolicos = cantidad_total - cantidad_fechas - cantidad_altos

    if cantidad_fechas + cantidad_altos + cantidad_simbolicos > cantidad_total:
        cantidad_simbolicos -= 1

    fechas = random.sample(range(1, 32), min(cantidad_fechas, 31))
    altos = random.sample(range(32, 70), min(cantidad_altos, 38))
    simbolicos = random.sample(base_numbers, min(cantidad_simbolicos, len(base_numbers)))

    combinacion = list(set(fechas + altos + simbolicos))

    while len(combinacion) < cantidad_total:
        n = random.randint(1, 69)
        if n not in combinacion:
            combinacion.append(n)

    return sorted(combinacion)

cantidad_numeros = st.slider("¿Cuántos números querés en cada combinación?", 2, 10, 6)
cantidad_jugadas = st.slider("¿Cuántas combinaciones querés generar?", 1, 50, 5)

if st.button("🎰 Generar combinaciones"):
    with st.spinner('🎱 Girando el bolillero...'):
        animation_html = '''
        <div style="display:flex;justify-content:center;align-items:center;padding:20px">
            <img src="https://media.giphy.com/media/3o6ZtpxSZbQRRnwCKQ/giphy.gif" width="150">
        </div>
        '''
        components.html(animation_html, height=200)
        time.sleep(2)

    st.markdown("### 🎯 Tus combinaciones:")

    jugadas = [generar_combinacion(cantidad_numeros) for _ in range(cantidad_jugadas)]
    for i, jugada in enumerate(jugadas, 1):
        st.success(f"Jugada #{i}: {jugada}")
