
import requests
from bs4 import BeautifulSoup

def getWebRequest(url):
	"""
	"""
	res = requests.get(url)
	res.raise_for_status()
	return res

def getWebLinkElems(requests):
	"""
	
	"""
	link = BeautifulSoup(requests.text, "html5lib")
	linkElems = link.find_all('a')
	linkAttr = []

	for l in linkElems:
		linkAttr.append(l.attrs['href'])

	return linkAttr

def testLinks(links):
        success = 0
        for link in links:
                try:
                        res = requests.get(link)
                        if res.status_code == requests.codes.ok:
                                print("Testing URL: " + link)
                                print("Response code: " + str(res.status_code))
                                success += 1
                        else:
                                print("ERROR. Response code: " + str(res.status_code))                 
                except requests.exceptions.MissingSchema:
                        print('Invalid url: ' + link)
                        pass
        return success

print("Enter web url: ")
url = str(input())
req = getWebRequest(url)
links = getWebLinkElems(req)

totalLinks = len(links)
successful = testLinks(links)

print("Test completed.")
print(str(successful) + " links out of " + str(totalLinks) + " successful.")

