import time

from board import SCL,SDA
import busio
import adafruit_ina219

#i2c_bus=busio.I2C(SCL,SDA)
#ina219=adafruit_ina219.INA219(i2c_bus)
#print("ina219 init")
#print(ina219)


class currentRead():
        
        def __init__(self):
                
            i2c_bus=busio.I2C(SCL,SDA)
            self.ina219 =adafruit_ina219.INA219(i2c_bus)
            print("ina219 init")
            print(self.ina219)  
            
               
               

        def currentReading(self):
            
            #print("Current:       {} mA".format(ina219.current/10))
            return self.ina219.current/10
            
            
        def voltageReading(self):
                
            return self.ina219.bus_voltage
                
    
    
#counter=0

    #print(ina219.gain)
    #print("Bus Voltage:   {} V".format(ina219.bus_voltage))
    #print("Shunt Voltage: {} mV".format(ina219.shunt_voltage / 1000))
    #print("Load Voltage:  {} V".format(ina219.bus_voltage  +  ina219.shunt_voltage))
    #print("Current:       {} mA".format(ina219.current/10))
    #print("Power:         {} W".format(ina219.power/10))
    #print("")
    
    #time.sleep(0.5)
    #counter=counter+1
    #if(counter>=4):
    #    counter=0
    #    time.sleep(2)
    
    
    
    
    
