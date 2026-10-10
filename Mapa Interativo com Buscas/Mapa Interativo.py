import folium
from folium.plugins import Geocoder
import os
import webbrowser

def criar_mapa():
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_arquivo = os.path.join(diretorio_atual, "mapa_interativo_busca.html")

    # Criar mapa sem tile padrão
    mapa = folium.Map(
        location=[15, 0],
        zoom_start=2,
        tiles=None  # Sem tile padrão
    )

    # Usar tile do ESRI (funciona sempre, sem bloqueio)
    folium.TileLayer(
        tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}',
        attr='Tiles &copy; Esri',
        name='Esri World Street Map',
        overlay=False,
        control=True
    ).add_to(mapa)

    # Alternativa 2: Stamen TonerLite (bem minimalista)
    folium.TileLayer(
        tiles='https://stamen-tiles-{s}.a.ssl.fastly.net/toner-lite/{z}/{x}/{y}.png',
        attr='Map tiles by Stamen Design, under CC BY 3.0. Data by OpenStreetMap, under ODbL.',
        name='Stamen Toner Lite',
        overlay=False,
        control=True
    ).add_to(mapa)

    # Adicionar controle de camadas
    folium.LayerControl().add_to(mapa)

    # Geocoder (busca)
    Geocoder(
        collapsed=False,
        position='topleft',
        add_marker=True
    ).add_to(mapa)

    mapa.save(caminho_arquivo)
    print(f"Mapa criado com sucesso em: {caminho_arquivo}")
    webbrowser.open('file://' + caminho_arquivo)

if __name__ == "__main__":
    criar_mapa()
