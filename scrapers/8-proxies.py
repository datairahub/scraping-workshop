import csv
import urllib2
import random
from bs4 import BeautifulSoup

proxies_list = [
    '180.242.67.8:8080',
    '159.89.208.224:8118',
    '36.89.51.205:8080',
]

outputpath = 'links.csv'

with open(outputpath, 'w') as outfile:

    writer = csv.writer(outfile)
    for counter in range(1,2):

        url = 'https://www.meneame.net/?page='+str(counter)

        # Set random proxy
        proxies = {
            'http': proxies_list[random.randint(0, len(proxies_list)-1)]
        }

        urllib2.install_opener(
            urllib2.build_opener(
                urllib2.ProxyHandler(proxies)
            )
        )
        response = urllib2.urlopen(url)
        html = response.read()


        # Get links
        soup = BeautifulSoup(html, "html.parser")
        links = soup.select('.news-summary .comments')

        for link in links:
            url = 'http://www.meneame.net' + link.get('href')
            print url
            writer.writerow([url])
