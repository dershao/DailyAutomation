import requests, json, sys


API_key = "a78cb5de3d831abd304abb2ff1d0dcc0"


def requestWeatherData(city, country):

	res = requests.get("http://api.openweathermap.org/data/2.5/weather?q=" + city + "," + country  + "&appid=" + API_key)
	res.raise_for_status()
	return res

def loadWeatherJson(request):

	weatherJson = json.loads(request.text)

	return weatherJson

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



def main():

	if (len(sys.argv) >= 2):
		city = sys.argv[1]
		country = sys.argv[2]
	else:
		city = str(input("Enter a city: "))
		country = str(input("Enter a country: "))

	weatherRes = requestWeatherData(city, country)
	weatherJson = loadWeatherJson(weatherRes)

	displayWeatherData(weatherJson)



if __name__ ==  "__main__":
	main()