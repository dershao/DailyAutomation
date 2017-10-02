#google image downloader

import requests
from selenium import webdriver

def main():

	print("Search Google images...")
	query = str(input())

	browser = webdriver.Firefox()
	browser.get("http://www.google.com/images")

	#TODO: find html idfor the search bar

	search = browser.find_element_by_id("tsf")
	search.send_keys(query)
	search.submit()

	#TODO: iterate through all images found from serach
	#TODO: download all 

def getImgRequest(url):
	res = requests.get(url)

def downloadImg(requests):

	img = open("googleimage.png", "wb")

	for chunk in requests.iter_content(100000):
		img.write(chunk)

	img.close()


if __name__ == "__main__":
	#opening program 
	main()

	pause = str(input("Press <ENTER> to continue..."))
