import csv
import urllib2
from bs4 import BeautifulSoup

outputpath = 'links.csv'

with open(outputpath, 'w') as outfile:

    writer = csv.writer(outfile)
    for counter in range(1,2):

        url = 'https://www.meneame.net/?page='+str(counter)

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
        }

        # Get URL
        response = urllib2.Request(url, headers=headers)
        pagedata = urllib2.urlopen(response)
        html = pagedata.read()

        # Get links
        soup = BeautifulSoup(html, "html.parser")
        links = soup.select('.news-summary .comments')

        for link in links:
            url = 'http://www.meneame.net' + link.get('href')
            print url
            writer.writerow([url])
