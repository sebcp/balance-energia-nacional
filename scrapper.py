from bs4 import BeautifulSoup

import requests

def download_files(link):
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    cards = soup.find_all(class_="card-grid")
    for card in cards:
        title = card.find(class_="titulo-dataset").get("title")
        if "Balance Nacional de Energía " in title:
            link = card.find("a").get("href")
            year = title.split(" ")[-1]
            data = requests.get(link)
            open(f"files/bne_{year}.xlsx", "wb").write(data.content)

download_files("http://energiaabierta.cl/categorias-estadistica/balance-energetico/")
download_files("http://energiaabierta.cl/categorias-estadistica/balance-energetico/?sf_paged=2")