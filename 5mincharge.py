import ADS1256
import time
import RPi.GPIO as GPIO

ADC = ADS1256.ADS1256()
ADC.ADS1256_init()

port = 0

relaywirelesscharge=24
relaybatt=23
GPIO.setmode(GPIO.BCM)             
GPIO.setup(relaywirelesscharge, GPIO.OUT)  
GPIO.setup(relaybatt          , GPIO.OUT)  
                
GPIO.output(relaybatt          , GPIO.HIGH) #battery
GPIO.output(relaywirelesscharge, GPIO.HIGH)



x=0
while True:
#for x in range(300):

	
	
	reading=round(ADC.ADS1256_GetChannalValue(port)*5.0/0x7fffff,2)
	print("Sec: "+str(x)+", Volts: "+str(reading))
	x=x+1
	time.sleep(1)
	if reading>4:
		print("Ending charge at: "+str(reading)+" V")
		break


GPIO.output(relaywirelesscharge, GPIO.LOW)  
GPIO.output(relaybatt	       , GPIO.LOW)  
GPIO.cleanup()
time.sleep(2)             
