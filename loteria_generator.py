
import random
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Generador Estratégico de Números para Lotería", layout="centered")
st.title("🎯 Generador Estratégico de Números para Lotería – Modo Intención")

with st.expander("ℹ️ ¿Cómo funciona esta app?"):
    st.markdown("""
    Bienvenido al **Generador Estratégico de Números para Lotería**: una herramienta diseñada para quienes buscan ir más allá del azar.

    Esta app une **inteligencia simbólica, análisis estadístico y lógica energética** para ayudarte a elegir tus combinaciones de forma más consciente y personalizada.

    ### 🔍 Lógica detrás del generador
    - **Números personales (1–31):** reflejan fechas que suelen tener valor emocional o familiar.
    - **Números altos (32–69):** reducen la repetición de patrones comunes. Te ayudan a salir del promedio.
    - **Números simbólicos:** seleccionados por su carga energética y cultural. Están asociados a arquetipos, numerología y significado emocional.

    Cada combinación incluye una selección equilibrada entre estos tres tipos, adaptada a tu intención.

    ### ✨ ¿Qué es el Modo Intención?
    Elegí cómo querés vibrar con tus jugadas. Cada intención modifica el criterio de selección numérica:

    - 🔥 **Audacia:** jugadas con extremos. Más números bajos o altos, para quienes apuestan fuerte y sin miedo.
    - 🧘 **Equilibrio:** combinaciones balanceadas, sin extremos. Ideal si buscás armonía y estabilidad.
    - 🌑 **Misterio:** foco en los números simbólicos. Ideal si seguís tu intuición, creés en señales y energías.
    - 🎯 **Precisión:** selección pura, lógica matemática sin repeticiones ni adornos. Para mentes estratégicas.

    ### 🎲 ¿Por qué usar esta app?
    Porque jugar con intención cambia el juego. Este generador no solo te da números, sino una experiencia con sentido.

    Cada jugada es **única, inteligente y simbólicamente cargada**. Es para vos, si querés algo más que azar.
    """)

intencion = st.selectbox("🌟 Elegí tu intención para esta jugada:", ["Equilibrio", "Audacia", "Misterio", "Precisión"])

base_numbers = [3, 5, 7, 9, 11, 13, 17, 21, 22, 27, 29, 31, 33, 36, 39, 41, 44, 47, 51, 55, 60, 63, 66, 69]
mensajes_simbolicos = {
    3: "Equilibrio sagrado: mente, cuerpo y alma.",
    5: "Movimiento, libertad y cambios positivos.",
    7: "Tu 7 protege. Guía invisible.",
    9: "Cierre de ciclo. Dejá atrás lo viejo.",
    11: "Número maestro. Puerta de intuición.",
    13: "El 13 no es mala suerte, es rebelión.",
    17: "Claridad y renacimiento.",
    21: "Completitud: el mundo te acompaña.",
    22: "El loco rompe la norma. Apostá sin miedo.",
    27: "Sensibilidad creativa. Conectá con lo sutil.",
    29: "Dualidad resuelta. Sos más fuerte que ayer.",
    31: "El fin de un ciclo abre uno nuevo.",
    33: "Número maestro. Conecta con lo alto.",
    36: "Fuerza emocional. Tiempo de sanar.",
    39: "Sabiduría en acción.",
    41: "Madurez y visión. Sabés lo que hacés.",
    44: "Estabilidad con poder. Base firme.",
    47: "Encuentro inesperado. Estás listo.",
    51: "Expansión interna. Crecé desde vos.",
    55: "Transformación rápida. Mantené el foco.",
    60: "Apertura espiritual. Abrite a lo nuevo.",
    63: "Cosecha espiritual. Recolectás lo sembrado.",
    66: "Maestría emocional. Liderazgo sensible.",
    69: "Dualidad, atracción, placer. Un número magnético."
}

mensajes_intencion = {
    "Audacia": "🔥 Jugada con extremos. Atrevida, desafiante, sin miedo.",
    "Equilibrio": "🧘 Jugada balanceada. Ni muy alto ni muy bajo.",
    "Misterio": "🌑 Jugada cargada de simbolismo. Para quien escucha señales.",
    "Precisión": "🎯 Jugada exacta. Nada librado al azar.",
}

def generar_combinacion(cantidad_total, intencion):
    numeros = set()
    if intencion == "Audacia":
        extremos = list(range(1, 11)) + list(range(60, 70))
        numeros.update(random.sample(extremos, min(2, cantidad_total)))
    elif intencion == "Equilibrio":
        medios = list(range(20, 51))
        numeros.update(random.sample(medios, min(3, cantidad_total)))
    elif intencion == "Misterio":
        numeros.update(random.sample(base_numbers, min(3, cantidad_total)))
    elif intencion == "Precisión":
        return sorted(random.sample(range(1, 70), cantidad_total))

    while len(numeros) < cantidad_total:
        numeros.add(random.randint(1, 69))
    return sorted(numeros)

def mostrar_animacion(jugada):
    bolas_html = "".join(
        [f'<div class="bola" style="animation-delay: {i*0.3}s;">{n}</div>' for i, n in enumerate(jugada)]
    )
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
        {bolas_html}
    </div>
    """
    components.html(animacion_html, height=200 + (len(jugada) // 5) * 70)

cantidad_numeros = st.slider("¿Cuántos números querés en cada combinación?", 2, 10, 6)
cantidad_jugadas = st.slider("¿Cuántas combinaciones querés generar?", 1, 20, 3)

if st.button("🎰 Generar combinaciones"):
    st.markdown(f"### ✨ Jugadas en modo: **{intencion}**")
    st.info(mensajes_intencion[intencion])
    for i in range(cantidad_jugadas):
        components.html("""
        <audio autoplay>
            <source src="https://www.soundjay.com/button/sounds/button-29.mp3" type="audio/mpeg">
        </audio>
    """, height=0)
        jugada = generar_combinacion(cantidad_numeros, intencion)
        st.subheader(f"Jugada #{i+1}")
        mostrar_animacion(jugada)
        for n in jugada:
            if n in mensajes_simbolicos:
                st.caption(f"🔮 **{n}** — {mensajes_simbolicos[n]}")
