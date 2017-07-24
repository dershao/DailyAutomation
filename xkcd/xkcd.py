#downloads xkcd comic

import requests, bs4, datetime

def getPage():
	res = requests.get('http://www.xkcd.com')
	res.raise_for_status()
	return res

def createSoup(request):
	xkcdSoup = bs4.BeautifulSoup(request.text)
	imgElems = xkcdSoup.select('img')
	url = imgElems[1].get('src')
	return url

def mkImgRequest(url):
	imgRes = requests.get('http:' + url)
	return imgRes

	

today = datetime.date.today()
page = getPage()
imgUrl = createSoup(page)
image = mkImgRequest(imgUrl)

todayExtension = today.strftime('%Y_%m_%d')

xkcd_comic = open('xkcd_' + todayExtension + '.png', 'wb')

for chunk in image.iter_content(100000):
	xkcd_comic.write(chunk)

xkcd_comic.close()

