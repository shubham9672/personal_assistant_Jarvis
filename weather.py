#pip install simplejson
import requests, json
#import sr
# Enter your API key here
api_key = "create your api key from openweathermap.org"

# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"
def weather(city_name):
	try:
		complete_url = base_url + "appid=" + api_key + "&q=" + city_name
		response = requests.get(complete_url)
		x = response.json()
		if x["cod"] != "404":
			y = x['main']
			current_temperature = y["temp"]
			current_pressure = y["pressure"]
			current_humidiy = y["humidity"]

			z = x["weather"]

			weather_description = z[0]["description"]
			a=[]
		    # print following values
			a.append(" current Temperature in kelvin is " +
		                    str(current_temperature))
		    #print(a)
			a.append(" with atmospheric pressure " + str(current_pressure)+"hPa")
			a.append(" having humidity " +str(current_humidiy)+"percent" )
			a.append(" overall weather is  " +str(weather_description))
			print(a)
			from win32com.client import Dispatch
			speak = Dispatch("SAPI.Spvoice")
			speak.Speak(a)
		  
		else:
		    print(" City Not Found ")
	except:
	 	print(" ")
if __name__ == '__main__':
    # function call
	weather()
