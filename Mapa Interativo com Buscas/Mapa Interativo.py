import folium
from folium.plugins import Geocoder
import os
import webbrowser

def criar_mapa():
    # 1. Localização do arquivo no seu drive E:
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_arquivo = os.path.join(diretorio_atual, "mapa_interativo_busca.html")

    # 2. Criar o mapa com o estilo 'Voyager' (Oceanos azuis e mais detalhes)
    mapa = folium.Map(
        location=[0, 0], 
        zoom_start=2,
        tiles='CartoDB voyager', # Este estilo traz as cores clássicas de mapa
        attr='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>'
    )

    # 3. Adicionar a barra de busca
    Geocoder(
        collapsed=False, 
        position='topleft', 
        add_marker=True
    ).add_to(mapa)

    # 4. Salvar o arquivo
    mapa.save(caminho_arquivo)
    
    print(f"Mapa atualizado com oceanos azuis em: {caminho_arquivo}")

    # 5. Abrir no navegador
    webbrowser.open('file://' + caminho_arquivo)

if __name__ == "__main__":
    criar_mapa()