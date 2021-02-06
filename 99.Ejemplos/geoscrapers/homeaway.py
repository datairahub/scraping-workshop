# -*- coding: UTF-8 -*-
import time, json
from urllib import request as urllib
from termcolor import colored


# San Sebastián
# python3 -c "from homeaway import homeaway_geoscraping; homeaway_geoscraping(43.34,-1.96,43.28,-2.02)"

def save_anunces(jsondata):
    base_url = 'https://www.homeaway.es'

    for anunce in jsondata['results']['hits']:
        apartment_url = base_url + anunce['detailPageUrl']

        print(colored(apartment_url +' '+ str(anunce['geoCode']['longitude']) +' '+ str(anunce['geoCode']['latitude']), 'magenta'))


def parse_response_json(url):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    }

    try:
        web = urllib.Request(url, headers=headers)
        web = urllib.urlopen(web).read()
        web = web.decode('utf-8')
        return {'status': True, 'response': json.loads(web)}

    except Exception as e:
        print(colored('Error parseando web', 'red'), e)
        return {'status': False, 'response': 0}


def divide_area(ne_lat, ne_lng, sw_lat, sw_lng):
    subareas = []
    cc_lng = sw_lng + ((ne_lng - sw_lng)/2)
    cc_lat = sw_lat + ((ne_lat - sw_lat)/2)

    subareas.append([round(cc_lat,5), round(cc_lng,5), round(sw_lat,5), round(sw_lng,5)]) # división SO
    subareas.append([round(cc_lat,5), round(ne_lng,5), round(sw_lat,5), round(cc_lng,5)]) # división SE
    subareas.append([round(ne_lat,5), round(cc_lng,5), round(cc_lat,5), round(sw_lng,5)]) # división NO
    subareas.append([round(ne_lat,5), round(ne_lng,5), round(cc_lat,5), round(cc_lng,5)]) # división NE

    return subareas


def homeaway_geoscraping(lat_ne, lon_ne, lat_so, lon_so):

    areas_por_analizar = [[lat_ne, lon_ne, lat_so, lon_so]]
    areas_divididas = []
    max_resultado = 5000

    def iterate_area(lat_noreste, lon_noreste, lat_suroeste, lon_suroeste):
        pagenum = 1
        try:
            api_url = 'https://www.homeaway.es/ajax/map/search/refined/@'+str(lat_suroeste)+','+str(lon_suroeste)+','+str(lat_noreste)+','+str(lon_noreste)+',18z/page:'+str(pagenum)
            time.sleep(1)
            jsondata = parse_response_json(api_url)

            if jsondata['response']:
                count = jsondata['response']['results']['hitCount']
                pages = jsondata['response']['results']['pageCount']

                if count == 0:
                    print('Área vacía')

                elif count < max_resultado:
                    print(colored('Menos de '+str(max_resultado)+' resultados, iniciando paginación','green'))
                    print('Guardando página ' + str(pagenum) + ' de ' +str(pages))
                    save_anunces(jsondata['response'])

                    while pagenum < pages:
                        pagenum = pagenum + 1
                        print('Guardando página ' + str(pagenum) + ' de ' +str(pages))
                        time.sleep(1)
                        jsondata = parse_response_json('https://www.homeaway.es/ajax/map/search/refined/@'+str(lat_suroeste)+','+str(lon_suroeste)+','+str(lat_noreste)+','+str(lon_noreste)+',18z/page:'+str(pagenum))
                        save_anunces(jsondata['response'])

                        if jsondata['response']['results']['isLastSearchablePage'] == True:
                            print('Última página')
                            break

                else:
                    print('Más de '+str(max_resultado)+' resultados, dividiendo área...')
                    for area in divide_area(lat_noreste, lon_noreste, lat_suroeste, lon_suroeste):
                        areas_divididas.append(area)
            else:
                print(colored('HTTP response False', 'red'))

        except Exception as e:
            print(colored('Error en iteraccion','red'), e)


    # area iteration
    while True:
        try:
            contador = 0
            for area in areas_por_analizar:
                contador = contador + 1
                print(colored('Area '+str(contador)+' de '+str(len(areas_por_analizar)),'blue'))
                iterate_area(area[0],area[1],area[2],area[3])

            areas_por_analizar = areas_divididas
            if len(areas_por_analizar) == 0:
                print(colored('Fin del programa','green'))
                break
            areas_divididas = []
            contador = 0
            print(colored('Reseteando arrays','cyan'))
            
        except Exception as e:
            print(colored('No se pudo iterar en el area','red'), e)
            break