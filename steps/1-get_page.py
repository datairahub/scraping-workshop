import urllib2

url = 'https://www.meneame.net/'

response = urllib2.Request(url)
pagedata = urllib2.urlopen(response)
html = pagedata.read()
print html