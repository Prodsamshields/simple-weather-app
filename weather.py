import requests
api_key = "f687732e838028c18d784e16dae1f7da"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = input("Enter location (city): ")
complete_url = base_url + "appid=" + "f687732e838028c18d784e16dae1f7da" + "&q=" + city_name
response = requests.get(complete_url)
x = response.json()

if x["cod"] != "404":
	y = x["main"]

	current_temperature = y['temp']
	z = x['weather']
	ktof = (int(current_temperature)-273.15) * 9/5 + 32 
	ktof2 = "{:.0f}".format(ktof)
	weather_description = z[0]['description']
	print('The temperature in', city_name, 'is currently:', str(ktof2), f"degrees Farenheit. The current condition is listed as {weather_description}.")
	

else:
	print(f"City \'{city_name}\' was not found in database.")