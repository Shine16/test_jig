import RPi.GPIO as GPIO
import time

relaywirelesscharge = 24
relaybatt = 23
GPIO.setmode(GPIO.BCM)             
GPIO.setup(relaywirelesscharge, GPIO.OUT)  
GPIO.setup(relaybatt          , GPIO.OUT)  
                
GPIO.output(relaybatt          , GPIO.HIGH) #battery
GPIO.output(relaywirelesscharge, GPIO.HIGH) #wireless charger
for x in range(300):
	print(x)
	time.sleep(1)

GPIO.output(relaywirelesscharge, GPIO.LOW)  
GPIO.output(relaybatt	       , GPIO.LOW)  
GPIO.cleanup()
time.sleep(2)             