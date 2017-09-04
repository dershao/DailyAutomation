#!/usr/bin/evn python3

import requests
from bs4 import BeautifulSoup

def getWebRequest(url):
    """
    param: param1: String

    return: requests
    Returns requests object of specified URL. 
    """
    res = requests.get(url)
    res.raise_for_status()
    return res

def getWebLinkElems(requests):
    """
    param: param1: requests

    return: list

    Returns list of links found on webpage by searching
    for <a> tags and <href> attributes.
    """
    link = BeautifulSoup(requests.text, "html5lib")
    linkElems = link.find_all('a')
    linkAttr = []

    for l in linkElems:
        linkAttr.append(l.attrs['href'])

    return linkAttr

def testLinks(links, webpage):
    """
    param: param1: list
    param: param2: String

    return: int

    Test each links found on webpage and returns
    the number of links that can successfully be connected.
    """
    success = 0
    for link in links:
        try:
            if link[0] == "/":
                link = webpage.__add__(link)

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

def pause():
    """
    return: None

    Prevents output from closing automatically
    """
    programPause = input("Press <ENTER> to exit...")


def main():

    print("Enter web url: ")
    url = str(input())
    req = getWebRequest(url)
    links = getWebLinkElems(req)

    totalLinks = len(links)
    successful = testLinks(links, url)

    print("Test completed")
    print(str(successful) + " links out of " + str(totalLinks) + " successful")



if __name__ == "__main__":

    main()
    pause()

