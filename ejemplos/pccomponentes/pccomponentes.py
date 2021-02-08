# -*- coding: UTF-8 -*-
import requests
import json

"""
Script para buscar por palabras en pc componentes y
mostrar nombre y precio de los resultados
"""

BUSQUEDA = 'pantalla hd'

headers = {
    'accept': 'application/json',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ca-ES,ca;q=0.9,es;q=0.8,en;q=0.7,gl;q=0.6,fr;q=0.5,la;q=0.4,da;q=0.3',
    'Connection': 'keep-alive',
    'Content-Length': '306',
    'content-type': 'application/x-www-form-urlencoded',
    'Host': 'bewoyx1cf1-dsn.algolia.net',
    'Origin': 'https://www.pccomponentes.com',
    'Referer': 'https://www.pccomponentes.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
}

url = 'https://bewoyx1cf1-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20vanilla%20JavaScript%20(lite)%203.32.0%3Binstantsearch.js%203.0.0%3BJS%20Helper%202.26.1&x-algolia-application-id=BEWOYX1CF1&x-algolia-api-key=47978d8b445ceaceb718dd842d434099&x-algolia-usertoken=anonymous-e1e83c34-588f-48ff-8c3c-99e201f0610f'

busqueda = BUSQUEDA.replace(' ', '%20')

for n in range(3):
    data = {
        "requests": [{
            "indexName":"pccomponentes:es",
            "params":"query="+busqueda+"&maxValuesPerFacet=20&page="+str(n+1)+"&highlightPreTag=__ais-highlight__&highlightPostTag=__%2Fais-highlight__&clickAnalytics=true&enablePersonalization=true&facets=%5B%22price.amount%22%2C%22brand.name%22%2C%22family.name%22%5D&tagFilters=",
        }]
    }

    r = requests.post(url, data=json.dumps(data), headers=headers)
    response = json.loads(r.content)
    resultados = response['results'][0]['hits']

    for resultado in resultados:
        print(resultado['price']['amount'], '-', resultado['title'])
        print('')