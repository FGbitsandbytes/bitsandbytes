#!/usr/bin/python 

#from sense_hat import SenseHat 
import time 
import sys
from gpiozero import CPUTemperature, LoadAverage, DiskUsage
from ISStreamer.Streamer import Streamer
from os import system, name

#sense = SenseHat()
logger = Streamer(bucket_name="Raspberry Pi 3B+ monitor", access_key="ist_nQKa6p-JBRWjZd0h1IIL6xvyOi5cSfeT")
#sense.clear()

try:
	while True:
		cpu = CPUTemperature()
		#temp = sense.get_temperature()
		#temp = round(temp, 1)
		print("Temperature CPU",cpu.temperature)
		logger.log("Temperature CPU",cpu.temperature)

		#humidity = sense.get_humidity()
            	#humidity = round(humidity, 1)  
		load = LoadAverage()
            	print("CPU Load :",load.load_average)  
		logger.log("CPU Load :",load.load_average)

            	#pressure = sense.get_pressure()
            	#pressure = round(pressure, 1)
		disk = DiskUsage()
            	print("DiskUsage",disk.usage)
		logger.log("DiskUsage",disk.usage)

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
