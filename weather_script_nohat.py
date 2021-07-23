#!/usr/bin/python

import requests, json, time, sys 
from ISStreamer.Streamer import Streamer
from os import system, name

#Since the hat should be delivered by UPS and they missed me
#I've decided to utilize an external weather API to feed the data to out API.

api_key = "yourAPI"
city = "Eindhoven"
url = "https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s&units=metric" % (city, api_key)
logger = Streamer(bucket_name="Weather Data", bucket_key="bucket key", access_key="access key")


try:
        while True:
		response = requests.get(url)
		data = json.loads(response.text)

		main = data['main']
		temperature = main['temp']
		temp_feel_like = main['feels_like']
		humidity = main['humidity']
		pressure = main['pressure']

		logger.log("Temperature C: ",temperature)
		logger.log("Feels like: ",temp_feel_like)
		logger.log("Humidity :",humidity)
		logger.log("Pressure:",pressure)

		time.sleep(5)
except KeyboardInterrupt:
        pass


