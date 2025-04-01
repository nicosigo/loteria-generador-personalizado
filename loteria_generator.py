
import random
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Generador Estratégico de Números para Lotería", layout="centered")
st.title("🎯 Generador Estratégico de Números para Lotería – Modo Intención")

with st.expander("ℹ️ ¿Cómo funciona esta app?"):
    st.markdown("Genera combinaciones inteligentes según tu intención.")

raw_intencion = st.selectbox("🌟 Elegí tu intención:", ["🧘 Equilibrio", "🔥 Audacia", "🌑 Misterio", "🎯 Precisión"])
intencion = raw_intencion.split()[1]

def generar_combinacion(cantidad_total):
    return sorted(random.sample(range(1, 70), cantidad_total))

def mostrar_animacion(jugada):
    bolas_html = "".join(
        [f'<div class="bola-glass" style="animation-delay: {i*0.15}s;"><span>{n}</span></div>' for i, n in enumerate(jugada)]
    )
    animacion_html = f'''
    <style>
    @keyframes popin {{
        0% {{ transform: scale(0.5); opacity: 0; }}
        70% {{ transform: scale(1.15); opacity: 1; }}
        100% {{ transform: scale(1); opacity: 1; }}
    }}
    .bola-glass {{
        display: inline-block;
        background: radial-gradient(circle at 30% 30%, #ffffff, #e0e0e0);
        box-shadow: inset 0 0 5px rgba(0,0,0,0.1), 0 6px 20px rgba(0,0,0,0.2);
        border-radius: 50%;
        width: 80px;
        height: 80px;
        line-height: 80px;
        text-align: center;
        margin: 12px;
        animation: popin 0.6s ease-out forwards;
        opacity: 0;
    }}
    .bola-glass span {{
        color: #111;
        font-size: 28px;
        font-weight: 700;
    }}
    .container {{
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        padding: 30px;
        gap: 10px;
    }}
    </style>
    <div class="container">{bolas_html}</div>
    '''
    components.html(animacion_html, height=240)

cantidad_numeros = st.slider("¿Cuántos números querés?", 2, 10, 6)
cantidad_jugadas = st.slider("¿Cuántas jugadas?", 1, 10, 3)

if st.button("🎰 Generar combinaciones"):
    st.subheader(f"Jugadas en modo: {raw_intencion}")
    for i in range(cantidad_jugadas):
        jugada = generar_combinacion(cantidad_numeros)
        st.write(f"### Jugada #{i+1}")
        mostrar_animacion(jugada)
