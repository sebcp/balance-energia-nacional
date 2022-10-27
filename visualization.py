from bs4 import BeautifulSoup
import pandas as pd
import plotly.express as px

def plot_secciones(path, title):
    df_secciones = pd.read_csv(path)
    df_secciones = df_secciones.rename(columns={"anio": "Año", "seccion": "Energético", "tcal": "Teracalorías"})
    fig = px.bar(df_secciones, x="Año", y="Teracalorías", color="Energético", title=title)
    return fig

fig_mineria_secciones = plot_secciones("files/bne_mineria_secciones.csv", "Consumo energético de minería según energético")
fig_industria_secciones = plot_secciones("files/bne_industrial_secciones.csv", "Consumo energético industrial según energético")
fig_transporte_secciones = plot_secciones("files/bne_transporte_secciones.csv", "Consumo energético de transporte según energético")
fig_no_industrial_secciones = plot_secciones("files/bne_no_industriales_secciones.csv", "Consumo energético público, residencial, comercial y sanitario según energético")

'''
with open("secciones_graph.html", "w+") as f:
    f.write(fig_mineria_secciones.to_html(full_html = False, include_plotlyjs="cdn"))
    f.write(fig_transporte_secciones.to_html(full_html = False, include_plotlyjs="cdn"))
    f.write(fig_industria_secciones.to_html(full_html = False, include_plotlyjs="cdn"))
    f.write(fig_no_industrial_secciones.to_html(full_html = False, include_plotlyjs="cdn"))
'''
html = """
<!DOCTYPE html>

<html lang="es">
<head>
</head>
<body>
<div class="grid-container">
    <div class="grid-cell" id="mineria">
    </div>
    <div class="grid-cell" id="industria">
    </div>
    <div class="grid-cell" id="transporte">
    </div>
    <div class="grid-cell" id="no-industrial">
    </div>
</div>
</body>
</html>
"""
soup = BeautifulSoup(html, "html.parser")
head = soup.head
head.append(soup.new_tag("script"))
head.script['src'] = "https://cdn.plot.ly/plotly-latest.min.js"
head.append(soup.new_tag("style", type="text/css"))
head.style.append(".grid-container {display: grid; grid-template-columns: repeat(2, 49vw); grid-gap: 15px;}")
head.style.append(".grid-cell {height: 45vh; border-radius: 3px;}")

div_mineria = soup.find("div", id="mineria")
div_mineria.append(BeautifulSoup(fig_mineria_secciones.to_html(full_html = False, include_plotlyjs=False), 'html.parser'))

div_industria = soup.find("div", id="industria")
div_industria.append(BeautifulSoup(fig_industria_secciones.to_html(full_html = False, include_plotlyjs=False), 'html.parser'))

div_transporte = soup.find("div", id="transporte")
div_transporte.append(BeautifulSoup(fig_transporte_secciones.to_html(full_html = False, include_plotlyjs=False), 'html.parser'))

div_no_industrial = soup.find("div", id="no-industrial")
div_no_industrial.append(BeautifulSoup(fig_no_industrial_secciones.to_html(full_html = False, include_plotlyjs=False), 'html.parser'))

with open("secciones_graph.html", "w+") as f:
    f.write(str(soup))