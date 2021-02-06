import urllib2
from bs4 import BeautifulSoup

url = 'https://www.dafont.com/es/theme.php?cat=301'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}

# Get URL
response = urllib2.Request(url, headers=headers)
pagedata = urllib2.urlopen(response)
html = pagedata.read()

# Get links
soup = BeautifulSoup(html, "html.parser")
links = soup.select('.lv1left')

print len(links)
