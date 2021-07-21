#!/usr/bin/python 

from sense_hat import SenseHat 
import time 
import sys
from os import system, name

sense = SenseHat()
sense.clear()

try:
	while True:
		temp = sense.get_temperature()
		temp = round(temp, 1)
		print("Temperature C",temp)

		humidity = sense.get_humidity()
            	humidity = round(humidity, 1)  
            	print("Humidity :",humidity)  

            	pressure = sense.get_pressure()
            	pressure = round(pressure, 1)
            	print("Pressure:",pressure)

		#added line in Fork
		sense.show_message("Temperature C:" + str(temp) + "Humidity:" + str(humidity) + "Pressure:" + str(pressure), scroll_speed=(0.08), back_color=[0,0,200])
		#end addition
		time.sleep(1)
		system('clear')
except KeyboardInterrupt:
	pass

#added line in Fork
sense.clear()
#end addition