import csv
import urllib2
from bs4 import BeautifulSoup

outputpath = 'links.csv'

with open(outputpath, 'w') as outfile:

    writer = csv.writer(outfile)
    for counter in range(1,5):

        url = 'https://www.meneame.net/?page='+str(counter)

        # Get URL
        response = urllib2.Request(url)
        pagedata = urllib2.urlopen(response)
        html = pagedata.read()

        # Get links
        soup = BeautifulSoup(html, "html.parser")
        links = soup.select('.news-summary .comments')

        for link in links:
            url = 'http://www.meneame.net' + link.get('href')
            print url
            writer.writerow([url])
