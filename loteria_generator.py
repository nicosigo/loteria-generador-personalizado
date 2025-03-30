
import random
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Generador Estratégico de Números para Lotería", layout="centered")

st.title("🎲 Generador Estratégico de Números para Lotería")
st.markdown("Esta app combina análisis estadístico, simbolismo cultural y estrategia para ayudarte a elegir combinaciones únicas y con sentido.")

with st.expander("ℹ️ ¿Cómo funciona esta app?"):
    st.markdown("""
    Esta app no genera números al azar sin más.

    Cada combinación que ves está construida con una **lógica pensada** para equilibrar:

    - **Números personales (1–31)**: representan fechas importantes. Aportan conexión emocional.
    - **Números altos (32–69)**: evitan repetir patrones comunes. Aumentan la exclusividad de tu jugada.
    - **Números simbólicos**: seleccionados por su carga energética, mística y cultural (ej. 7, 13, 22, 33, 41, 69).

    La proporción entre estos tres grupos se adapta automáticamente según la cantidad de números que elijas (entre 2 y 10).

    🔢 **Ejemplo (6 números):**
    - 2 del rango 1–31 (fechas)
    - 2 del rango 32–69 (números altos)
    - 2 del set simbólico

    Cada número se revela con una **animación tipo bolillero**, agregando suspenso y emoción.

    👉 Este sistema está diseñado para darte una experiencia única, con jugadas que no solo son diferentes... sino que tienen sentido.
    """)

base_numbers = [7, 13, 22, 33, 41, 69]
mensajes_simbolicos = {
    7: "Tu 7 protege. Guía invisible.",
    13: "El 13 no es mala suerte, es rebelión.",
    22: "El loco rompe la norma. Apostá sin miedo.",
    33: "Número maestro. Conecta con lo alto.",
    41: "Madurez y visión. Sabés lo que hacés.",
    69: "Dualidad, atracción, placer. Un número magnético.",
}
mensajes_generales = [
    "Esta jugada vibra con audacia.",
    "Equilibrio entre emoción y estrategia.",
    "Una combinación que no pasa desapercibida.",
    "Poder simbólico en tus manos.",
    "Azar con intención: la fórmula perfecta.",
]

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

def generar_carta_png(numeros, frases_dict):
    width, height = 800, 400
    fondo_color = (255, 255, 255)
    bolilla_color = (200, 200, 255)
    bolilla_outline = (50, 50, 150)
    texto_color = (0, 0, 0)

    img = Image.new("RGB", (width, height), color=fondo_color)
    draw = ImageDraw.Draw(img)

    n = len(numeros)
    diametro = 70
    espacio = 20
    total_anchura = n * diametro + (n - 1) * espacio
    start_x = (width - total_anchura) // 2
    y_bolillas = 80

    try:
        font_num = ImageFont.truetype("arial.ttf", size=32)
        font_frase = ImageFont.truetype("arial.ttf", size=20)
    except:
        font_num = ImageFont.load_default()
        font_frase = ImageFont.load_default()

    for i, num in enumerate(numeros):
        x = start_x + i * (diametro + espacio)
        draw.ellipse([x, y_bolillas, x + diametro, y_bolillas + diametro],
                     fill=bolilla_color, outline=bolilla_outline, width=3)
        num_str = str(num)
        bbox = draw.textbbox((0, 0), num_str, font=font_num)
        w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
        text_x = x + (diametro - w) / 2
        text_y = y_bolillas + (diametro - h) / 2
        draw.text((text_x, text_y), num_str, font=font_num, fill=texto_color)

    y_texto = y_bolillas + diametro + 30
    x_texto = 50
    for num in numeros:
        if num in frases_dict:
            frase = frases_dict[num]
            draw.text((x_texto, y_texto), f"{num}: {frase}", font=font_frase, fill=texto_color)
            y_texto += 25

    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    return buffer

cantidad_numeros = st.slider("¿Cuántos números querés en cada combinación?", 2, 10, 6)
cantidad_jugadas = st.slider("¿Cuántas combinaciones querés generar?", 1, 20, 3)

if st.button("🎰 Generar combinaciones"):
    st.markdown("### ✨ Tus combinaciones:")
    jugadas = [generar_combinacion(cantidad_numeros) for _ in range(cantidad_jugadas)]
    for i, jugada in enumerate(jugadas, 1):
        st.subheader(f"Jugada #{i}")
        mostrar_animacion(jugada)
        mensajes = [(n, mensajes_simbolicos[n]) for n in jugada if n in mensajes_simbolicos]
        if mensajes:
            for numero, texto in mensajes:
                st.caption(f"🔮 **{numero}** — {texto}")
        else:
            st.caption(f"🧠 {random.choice(mensajes_generales)}")

        carta_buffer = generar_carta_png(jugada, mensajes_simbolicos)
        st.download_button(
            label="📥 Descargar carta PNG",
            data=carta_buffer,
            file_name=f"jugada_{i}.png",
            mime="image/png"
        )
