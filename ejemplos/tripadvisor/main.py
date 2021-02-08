from urllib import request
import json
import csv

"""
Script para buscar en tripadvisor por coordenadas
"""

outputpath = 'links.csv'

url = 'https://www.tripadvisor.es/GMapsLocationController?&geo=1&mh=892&from=Restaurants&trackPageView=false&g=1&finalRequest=false&Action=update&mapProviderFeature=ta-maps-citymaps&mw=1880&mc=37.011615,-6.302735&mz=12&version=1.3.5&pinSel=v2&origLocId=1&validDates=false&includeMeta=false&sponsors='

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}

# Get URL
response = request.Request(url, headers=headers)
pagedata = request.urlopen(response)
response_read = pagedata.read()

response_json = json.loads(response_read)

for hotel in response_json['hotels']:
    print(
        hotel['customHover']['title'],
        hotel['lat'],
        hotel['lng'],
        '\n'
    )