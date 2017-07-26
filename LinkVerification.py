
import requests, bs4

def getWebRequest(url):
	"""
		str -> requests
		Returns the http request to a specified web url.
	"""
	res = requests.get(url) 
	return res

def getWebLinkElems(requests):
	"""
		Requests -> str list
	"""
	link = bs4.BeautifulSoup(requests.text)
	linkElems = link.select('a href')
	linkAttr = []

	for l in linkElems:
		linkAttr.append(l.get('a href'))

	return linkAttr

def requestLink(links):
	for link in links:
		print("Testing link: " + link)
		res = request.get(link)
		res.raise_for_status()
		print("Response code: " + str(res))

print("Enter web url: ")
url = str(input())
req = getWebRequest(url)
links = getWebLinkElems(req)
requestLink(links)

