import urllib2
from bs4 import BeautifulSoup

for counter in range(1,10):

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
