#!/usr/bin/python

from sense_hat import SenseHat
import time
import sys
from os import system, name
from ISStreamer.Streamer import Streamer

# pip3 install ISStreamer
# python3 --version

"""
bucket_name="WeatherStation"
access_key="ist_GDciofkAO0_L0fXCyOJVPNX249r4filC"
bucket_key="FGAVH5ETKLUG"
"""

sense = SenseHat()
#logger = Streamer(bucket_name="Sense Hat Sensor Data", access_key="ist_07z-dw6EXikEpZtO8wo46IPiZUb5T7U7", bucket_key="e3db7268-d7f1-446d-8e7f-3207937fdab3")
logger = Streamer(bucket_name="WeatherStation", access_key="ist_GDciofkAO0_L0fXCyOJVPNX249r4filC", bucket_key="FGAVH5ETKLUG")
sense.clear()

try:
	while True:
		temp = sense.get_temperature()
		temp = round(temp, 1)
		print("Temperature C",temp)
		logger.log("Temperature C",temp)

		humidity = sense.get_humidity()
		humidity = round(humidity, 1)
		print("Humidity :",humidity)
		logger.log("Humidity :",humidity)

		pressure = sense.get_pressure()
		pressure = round(pressure, 1)
		print("Pressure:",pressure)
		logger.log("Pressure:",pressure)

		#added line in Fork
		sense.show_message("Temperature C:" + str(temp) + " Humidity:" + str(humidity) + " Pressure:" + str(pressure), scroll_speed=(0.08), back_colour=[0,0,200])
		#end addition

		time.sleep(1)
		system('clear')

except KeyboardInterrupt:
	pass

#added line in Fork
sense.clear()
#end addition