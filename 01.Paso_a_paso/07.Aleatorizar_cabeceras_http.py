# Importamos las librerías
from urllib import request
from bs4 import BeautifulSoup
import csv
import random # <-- Nuevo módulo

# Definimos el nombre del archivo
outputpath = 'resultados.csv'

# Definimos las opciones de user agent para las cabeceras
user_agent_list = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'
]

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
        # Haciendo que escoja aleatoriamente el User-Agent
        headers = {
            'User-Agent': random.choice(user_agent_list), # <-- Escogerá una opción al azar
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
