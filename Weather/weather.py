#!/usr/bin/env python3

import requests, json, sys


API_key = "a78cb5de3d831abd304abb2ff1d0dcc0"


def displayWeatherData(mJson):

	name_city = mJson["name"].upper()
	name_country = mJson["sys"]["country"]
	cloudiness = mJson["weather"][0]["description"].capitalize()
	wind = str(mJson["wind"]["speed"]) + " m/s"
	high_temp = mJson["main"]["temp_max"] - 273
	low_temp = mJson["main"]["temp_min"] - 273

	print("\n")

	print("City: " + name_city + "\n")
	print("Country: " + name_country + "\n")

	print("====================================================\n") 
	
	print("General Weather\n")
	print("Cloudiness: " + cloudiness + "\n")
	print("Wind: " + wind + "\n")

	print("====================================================\n") 
	
	print("Temperature\n")
	print("High: " + str(round(high_temp, 2)) + "\n")
	print("Low: " + str(round(low_temp, 2)) + "\n")

def loadWeatherJson(request):

	weatherJson = json.loads(request.text)

	displayWeatherData(weatherJson)

def requestWeatherData(city, country):

	res = requests.get("http://api.openweathermap.org/data/2.5/weather?q=" + city + "," + country  + "&appid=" + API_key)
	res.raise_for_status()
	loadWeatherJson(res)

def locationPrompt():
	city = str(input("Enter a city: "))
	country = str(input("Enter a country: "))
	return (city, country)


def main():

	if (len(sys.argv) >= 2):
		city = sys.argv[1]
		country = sys.argv[2]
		requestWeatherData(city, country)
	else:
		while True:
			location = locationPrompt()
			requestWeatherData(location[0], location[1])
			
			again = str(input("Search weather data from new location? [Y/n]"))
			
			if again.upper() != "Y":
				break;

if __name__ ==  "__main__":
	main()