# Importamos las librerías
from urllib import request
from bs4 import BeautifulSoup
import csv

# Definimos el nombre del archivo
outputpath = 'resultados.csv'

# Abrimos el archivo para poder escribir en él
with open(outputpath, 'w') as outfile:

    # Definimos el "escritor"
    writer = csv.writer(outfile)

    # Definimos los números de cada página que queremos consultar,
    # en este caso serán las páginas 1, 2, 3 y 4
    for page_number in range(1,5):

        # Imprimimos por pantalla el número de página actual
        print('Página', page_number)

        # Definimos la url que queremos pedir
        url = 'https://www.meneame.net/?page='+str(page_number)

        # Definimos las cabeceras de nuestras peticiones http
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            'Content-Type': 'application/json; charset=UTF-8',
        }

        # Hacemos la petición con las cabeceras http
        response = request.Request(url, headers=headers)
        pagedata = request.urlopen(response)
        html = pagedata.read()

        # Leemos el html devuelto
        soup = BeautifulSoup(html, "html.parser")

        # Guardamos los enlaces a las noticias
        links = soup.select('.news-summary .comments')

        # Recorremos los resultados encontrados
        for link in links:
            # Añadimos la parte que falta a cada url
            url = 'http://www.meneame.net' + link.get('href')
            # Escribimos el enlace en el archivo
            writer.writerow([url])
