#!/usr/bin/evn python3

import sys, pyperclip, webbrowser

if (len(sys.argv) > 1):
	#get address from command line
	address = ''.join(sys.argv[1:])
else:
	#get address from copy
	address = pyperclip.paste()


webbrowser.open('http://www.google.com/maps/place/' + address)
