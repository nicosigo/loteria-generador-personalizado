
import random
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Bolillero Estratégico", layout="centered")

st.title("🎯 Bolillero Estratégico – Demo Visual 2.0")

st.markdown("Descubrí tus números uno por uno, con suspenso, sonido y sentido.")

jugada = sorted(random.sample(range(1, 70), 6))

animation_html = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        .container {{
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            margin-top: 40px;
        }}
        .bola {{
            width: 70px;
            height: 70px;
            margin: 10px;
            border-radius: 50%;
            background: radial-gradient(circle, #ffffff, #e0e0e0);
            border: 3px solid #4a4a4a;
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 24px;
            opacity: 0;
            transform: scale(0);
            animation: showUp 0.4s ease-out forwards;
        }}
        @keyframes showUp {{
            0% {{ transform: scale(0); opacity: 0; }}
            80% {{ transform: scale(1.2); opacity: 1; }}
            100% {{ transform: scale(1); }}
        }}
    </style>
</head>
<body>
<div class="container" id="bolillero"></div>

<audio id="sonido" src="https://cdn.pixabay.com/download/audio/2022/03/15/audio_c607ab9b90.mp3?filename=click-pop-2-185287.mp3"></audio>

<script>
    const jugada = {jugada};
    const container = document.getElementById('bolillero');
    const sonido = document.getElementById('sonido');

    jugada.forEach((num, i) => {{
        setTimeout(() => {{
            const bola = document.createElement('div');
            bola.className = 'bola';
            bola.style.animationDelay = `${{i * 0.5}}s`;
            bola.textContent = num;
            container.appendChild(bola);
            sonido.currentTime = 0;
            sonido.play();
        }}, i * 700);
    }});
</script>
</body>
</html>
"""

components.html(animation_html, height=300)
