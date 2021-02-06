# Importamos la librería para hacer peticiones http
from urllib import request

# Definimos la url que queremos pedir
url = 'https://www.meneame.net/'

# Hacemos la petición
response = request.Request(url)
pagedata = request.urlopen(response)
html = pagedata.read()

# Imprimimos en pantalla el resultado
print(html)