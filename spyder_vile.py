from urllib.request import urlopen
from bs4 import BeautifulSoup
import sys
import re


if len(sys.argv) != 2:
	print("usage %s URL" %(sys.argv[0]))
	sys.exit(0)


targetUrl = str(sys.argv[1])


def getInternalLinks(url):

	try:
		html = urlopen(url)
	except AttributeError as e:
		print(e)

	try:
		bsObj = BeautifulSoup(html.read())
	except AttributeError as e:
		print(e)


	internalLinks = []

	for link in bsObj.findAll("a"):
		if 'href' in link.attrs:
			print("[++]_INTERNAL LINKS_[++]"+link.attrs['href']+".")
			



def getExternalLinks(url):

	try:
		html = urlopen(url)
	except AttributeError as e:
		print(e)

	try:
		bsObj = BeautifulSoup(html.read())
	except AttributeError as e:
		print(e)


	externalLinks = []

	for link in bsObj.findAll("a", href=re.compile("^(http|www)((?!"+url+").)*$")):
		if link.attrs['href'] is not None:
			if link.attrs not in externalLinks:
				externalLinks.append(link.attrs['href'])
				print("[++]_EXTERNAL LINKS_[++]"+link.attrs['href']+".")




getInternalLinks(targetUrl)
getExternalLinks(targetUrl)
