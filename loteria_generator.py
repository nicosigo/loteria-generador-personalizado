
import random
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Generador Estratégico de Números para Lotería", layout="centered")

st.title("🎯 Generador Estratégico de Números para Lotería – Modo Intención")

st.markdown("Elegí tu energía antes de jugar. Cada modo ajusta la lógica de la combinación.")

# Selector de intención energética
intencion = st.selectbox(
    "🌟 Elegí tu intención para esta jugada:",
    ["Equilibrio", "Audacia", "Misterio", "Precisión"]
)

base_numbers = [7, 13, 22, 33, 41, 69]

mensajes_simbolicos = {
    7: "Tu 7 protege. Guía invisible.",
    13: "El 13 no es mala suerte, es rebelión.",
    22: "El loco rompe la norma. Apostá sin miedo.",
    33: "Número maestro. Conecta con lo alto.",
    41: "Madurez y visión. Sabés lo que hacés.",
    69: "Dualidad, atracción, placer. Un número magnético.",
}

mensajes_intencion = {
    "Audacia": "🔥 Jugada con extremos. Atrevida, desafiante, sin miedo.",
    "Equilibrio": "🧘 Jugada balanceada. Ni muy alto ni muy bajo.",
    "Misterio": "🌑 Jugada cargada de simbolismo. Para quien escucha señales.",
    "Precisión": "🎯 Jugada exacta. Nada librado al azar.",
}

mensajes_generales = [
    "Esta jugada vibra con audacia.",
    "Equilibrio entre emoción y estrategia.",
    "Una combinación que no pasa desapercibida.",
    "Poder simbólico en tus manos.",
    "Azar con intención: la fórmula perfecta.",
]

def generar_combinacion(cantidad_total, intencion):
    numeros = set()
    if intencion == "Audacia":
        extremos = list(range(1, 11)) + list(range(60, 70))
        numeros.update(random.sample(extremos, min(2, cantidad_total)))
    elif intencion == "Equilibrio":
        medios = list(range(20, 51))
        numeros.update(random.sample(medios, min(3, cantidad_total)))
    elif intencion == "Misterio":
        simbolicos = base_numbers
        numeros.update(random.sample(simbolicos, min(3, cantidad_total)))
    elif intencion == "Precisión":
        # Solo 1–69, sin repetir y bien distribuidos
        return sorted(random.sample(range(1, 70), cantidad_total))

    while len(numeros) < cantidad_total:
        n = random.randint(1, 69)
        numeros.add(n)
    return sorted(numeros)

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
    components.html(animacion_html, height=200 + (len(jugada) // 5) * 70)

cantidad_numeros = st.slider("¿Cuántos números querés en cada combinación?", 2, 10, 6)
cantidad_jugadas = st.slider("¿Cuántas combinaciones querés generar?", 1, 20, 3)

if st.button("🎰 Generar combinaciones"):
    st.markdown(f"### ✨ Jugadas en modo: **{intencion}**")
    st.info(mensajes_intencion[intencion])

    for i in range(cantidad_jugadas):
        jugada = generar_combinacion(cantidad_numeros, intencion)
        st.subheader(f"Jugada #{i+1}")
        mostrar_animacion(jugada)
        mensajes = [(n, mensajes_simbolicos[n]) for n in jugada if n in mensajes_simbolicos]
        if mensajes:
            for numero, texto in mensajes:
                st.caption(f"🔮 **{numero}** — {texto}")
        else:
            st.caption(f"🧠 {random.choice(mensajes_generales)}")
