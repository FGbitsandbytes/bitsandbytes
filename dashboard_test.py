#!/usr/bin/python 

#from sense_hat import SenseHat 
import time 
import sys
from ISStreamer.Streamer import Streamer
from os import system, name

#sense = SenseHat()
logger = Streamer(bucket_name="Sense Hat Sensor Data", access_key="ist_nQKa6p-JBRWjZd0h1IIL6xvyOi5cSfeT")
#sense.clear()

try:
	while True:
		#temp = sense.get_temperature()
		#temp = round(temp, 1)
		print("Temperature C","23.0")
		logger.log("Temperature C","23.0")

		#humidity = sense.get_humidity()
            	#humidity = round(humidity, 1)  
            	print("Humidity :","68%")  
		logger.log("Humidity :","68%")

            	#pressure = sense.get_pressure()
            	#pressure = round(pressure, 1)
            	print("Pressure:","1003")
		logger.log("Pressure:","1003")

		#added line in Fork
		#sense.show_message("Temperature C:" + str(temp) + "Humidity:" + str(humidity) + "Pressure:" + str(pressure), scroll_speed=(0.08), back_colour=[0,0,200])
		#end addition
		time.sleep(1)
		system('clear')
except KeyboardInterrupt:
	pass

#added line in Fork
#sense.clear()
#end addition
