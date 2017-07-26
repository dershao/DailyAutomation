#Business Insider - Tech Insider Article Opener

import requests, bs4, webbrowser

def getPage():
	"""
	Returns the request of specified URL.

	:returns: requests
	"""
	res = requests.get('http://www.businessinsider.com/sai')
	res.raise_for_status()
	return res

def createSoup(request):
	"""
	Returns bs4 object of url request.

	:param: param1: requests
	:returns: bs4.BeautifulSoup
	"""
	techSoup = bs4.BeautifulSoup(request.text)
	return techSoup

def getArticleLinks(bs4obj):
	"""
	Returns list of article links.

	:param: param1: bs4.BeautifulSoup
	:returns: list
	"""
	urls = []
	for h in bs4obj.find_all('h2'):
		a = h.find('a')
		urls.append(a.attrs['href'])
	return urls

def getMainArticleLink(bs4obj):
	"""
	Returns url of main article.

	:param: param1: bs4.BeautifulSoup
	:returns: String
	"""
	mainHeading = bs4obj.find('h1')
	a = mainHeading.find('a')
	return a.attrs['href']

page = getPage()
pageSoup = createSoup(page)
links = getArticleLinks(pageSoup)
main = getMainArticleLink(pageSoup)

#opens main article
webbrowser.open_new(main)

#open secondary articles
for i in range(1,4):
	webbrowser.open_new_tab(links[i])


