#!/usr/bin/python 

from sense_hat import SenseHat 
import time 
import sys
from ISStreamer.Streamer import Streamer
from os import system, name

sense = SenseHat()
logger = Streamer(bucket_name="Sense Hat Sensor Data", access_key="ist_hRrJBGvfDPasKHL5gsQt2DQYt93vvPlU")
sense.clear()

try:
	while True:
		temp = sense.get_temperature()
		temp = round(temp, 1)
		#print("Temperature C",temp)
		logger.log("Temperature C",temp)

		humidity = sense.get_humidity()
            	humidity = round(humidity, 1)  
            	#print("Humidity :",humidity)  
		logger.log("Humidity :",humidity)

            	pressure = sense.get_pressure()
            	pressure = round(pressure, 1)
            	#print("Pressure:",pressure)
		logger.log("Pressure:",pressure)

		#added line in Fork
		sense.show_message("Temperature C:" + str(temp) + " Humidity: " + str(humidity) + " Pressure: " + str(pressure), scroll_speed=(0.04), back_colour=[0,0,200])
		#end addition
		time.sleep(1)
		#system('clear')
except KeyboardInterrupt:
	pass

#added line in Fork
sense.clear()
#end addition
