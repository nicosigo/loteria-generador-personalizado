
import random
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Generador de Números para Lotería", layout="centered")

st.title("🎰 Generador de Números con Estilo Bolillero")
st.markdown("Esta versión incluye animaciones secuenciales para mostrar los números como si salieran de un bolillero o ruleta.")

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
cantidad_jugadas = st.slider("¿Cuántas combinaciones querés generar?", 1, 20, 3)

def mostrar_animacion(jugada):
    animacion_html = f"""
    <style>
    @keyframes drop {{
        0% {{ transform: translateY(-100px); opacity: 0; }}
        100% {{ transform: translateY(0); opacity: 1; }}
    }}
    .bola {{
        display: inline-block;
        background: radial-gradient(circle, #ffffff, #e0e0e0);
        border: 2px solid #ccc;
        border-radius: 50%;
        width: 60px;
        height: 60px;
        line-height: 60px;
        text-align: center;
        font-size: 24px;
        margin: 5px;
        animation: drop 0.5s ease forwards;
        opacity: 0;
    }}
    .container {{
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        padding: 20px;
    }}
    </style>
    <div class="container">
        {"".join([f'<div class="bola" style="animation-delay: {i*0.3}s;">{n}</div>' for i, n in enumerate(jugada)])}
    </div>
    """
    components.html(animacion_html, height=200 + (cantidad_numeros // 5) * 70)

if st.button("🎰 Generar combinaciones"):
    st.markdown("### ✨ Tus combinaciones:")

    jugadas = [generar_combinacion(cantidad_numeros) for _ in range(cantidad_jugadas)]
    for i, jugada in enumerate(jugadas, 1):
        st.subheader(f"Jugada #{i}")
        mostrar_animacion(jugada)
