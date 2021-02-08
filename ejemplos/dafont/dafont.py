from urllib import request
from bs4 import BeautifulSoup

"""
Script para listar todas las tipografías de Dafont
en la categoría Tecno > Cuadrado (cat=301)
"""

url = 'https://www.dafont.com/es/theme.php?cat=301'
font_url = 'https://www.dafont.com/es/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}

# Get URL
response = request.Request(url, headers=headers)
pagedata = request.urlopen(response)
html = pagedata.read()

# Get links
soup = BeautifulSoup(html, "html.parser")
links = soup.select('.lv1left')

for link in links:
    print('Name:', link.text.replace('  ', ' ')) # Print title
    print('Link:', font_url + link.select('a')[0]['href'])
    print()
