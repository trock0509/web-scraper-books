import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/"
response = requests.get(url)
response.encoding = "utf-8"

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    libros = soup.find_all("article", class_="product_pod")

    data = []

    for libro in libros:
        titulo = libro.h3.a["title"]
        precio = libro.find("p", class_="price_color").text
        data.append({
            "titulo": titulo,
            "precio": precio
        })

    df = pd.DataFrame(data)
    df.to_csv("libros.csv", index=False, encoding="utf-8-sig")

    print("Datos guardados correctamente")
else:
    print("Error al acceder a la página")