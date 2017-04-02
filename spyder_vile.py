
import urllib2

from bs4 import BeautifulSoup

import sys


urls = []
urls2 = []


target_url = sys.argv[1]


url = urllib2.urlopen(target_url).read()
soup = BeautifulSoup(url)


"""finding all 'a' tags on html, after that search for all href and extract all http tags"""
for line in soup.find_all('a'):
	newline = line.get('href')

	try:
		if newline[:4] == 'http':
			if target_url == newline:
				urls.append(str(newline))
		elif newline[:1] == '/':
			combline = target_url + newline
			urls.append(str(combline))		
	except:
		pass


for uurl in urls:
	url = urllib2.urlopen(uurl).read()
	soup = BeautifulSoup(url)

	for line in soup.find_all('a'):
		newline = line.get('href')

		try:
			if newline[:4] == "http":
				if target_url == newline:
					urls2.append(str(newline))
			elif newline[:1] == "/":
				combline = target_url + newline
				urls2.append(str(combline))
		except:
			pass



urls3 = set(urls2)

for value in urls3:
	print value
