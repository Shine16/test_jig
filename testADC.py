import ADS1256
import time
import RPi.GPIO as GPIO

ADC = ADS1256.ADS1256()
ADC.ADS1256_init()
port = 0

relaywirelesscharge=24
relaybatt=27
GPIO.setmode(GPIO.BCM)             
GPIO.setup(relaywirelesscharge, GPIO.OUT)  
GPIO.setup(relaybatt          , GPIO.OUT)  
                
GPIO.output(relaybatt          , GPIO.HIGH) #battery
GPIO.output(relaywirelesscharge, GPIO.HIGH)




while True:
	reading=round(ADC.ADS1256_GetChannalValue(port)*5.0/0x7fffff,2)
	print(reading)
	time.sleep(0.1)
	
