# Name = v. sai sudheer kumar
# mail id =saisudheer575@gmail.com

import requests
from datetime import datetime


Api_key = '683728a5f2d6216b3b0a8f948ab8fbf5'
# My API Key from openwethermap.org
Location = input("Enter the city name: ")
# tacking the location form the user.

Complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+Location+"&appid="+Api_key
Api_link = requests.get(Complete_api_link)
Api_data = Api_link.json()

#create variables to store and display data.
Temperature_city = ((Api_data['main']['temp']) - 273.15)
Weather_description = Api_data['weather'][0]['description']
Humidity = Api_data['main']['humidity']
Wind_speed = Api_data['wind']['speed']
Date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

info = open('TEMPERATUREDATA.txt','w')
# Creates a text file if doesn't exist or writes into the text file if it exist.

info.write("-------------------------------------------------------------\n")
info.write ("Weather Status at {}  on {}\n".format(Location.upper(), Date_time))
# for writing weather status of a particular place at particular time and date in to text file.
info.write ("-------------------------------------------------------------\n")

info.write("Current temperature is: {:.2f} deg C\n".format(Temperature_city))
# for writing current temperature in to text file.
info.write("Current weather desc  : {}\n".format(Weather_description))
# for writing current Weather in to text file.
info.write("Current Humidity      : {} %\n".format(Humidity))
# for writing current percentage of Humidity in to text file.
info.write("Current wind speed    : {} KMPH".format(Wind_speed))
# for writing current wind speed in to text file.
info.close()
# for closing the text file which has been opened.