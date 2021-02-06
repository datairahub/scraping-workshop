# Importamos la librería para hacer peticiones http
from urllib import request
# Importamos la librería para "enterder" el html
from bs4 import BeautifulSoup
# Importamos la librería para leer y escribir en csv
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

        # Hacemos la petición
        response = request.Request(url)
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
