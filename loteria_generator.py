

bolas_html = "".join(
    [f'<div class="bola" style="animation-delay: {{i*0.3}}s;">{{n}}</div>' for i, n in enumerate(jugada)]
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
