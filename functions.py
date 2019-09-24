import time
import ADS1256
import RPi.GPIO as GPIO


def testGPIO():
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(3, GPIO.IN)
         
        
        while(1):
                #print(GPIO.input(3))
                counter=0
                oldtime=0
                if (GPIO.input(3)==False):
                        oldtime=time.time()
                        while(GPIO.input(3)==False):
                                pass
                                #counter=counter+1
                        #print("sense"+str(counter))
                        print("Reset pulse of "+str(time.time()-oldtime)+" seconds")
                 

def singleRead():
        try:
                oldtime=time.time()
                ADC = ADS1256.ADS1256()
                if (ADC.ADS1256_init() == -1):
                        exit()  
                print("completed init")        
                ADC.ADS1256_SetChannal(0)
                print("completed init") 
                ADC.ADS1256_WriteCmd(ADS1256.CMD['CMD_SYNC'])
                ADC.ADS1256_WriteCmd(ADS1256.CMD['CMD_WAKEUP'])
                print("completed init") 
                
                while(1):                        
                        ADC_Value=ADC.ADS1256_Read_ADC_Data()
                        
                        #ADC_Value=ADC.ADS1256_GetChannalValue(0)
                        #print(ADC_Value)
                        #print(type(ADC_Value))
                        print(time.time()-oldtime)
                        oldtime=time.time()
                        
                        ADC_Value=ADC_Value*5.0/0x7fffff
                        if(ADC_Value>3):
                                print('H')   
                        elif(ADC_Value<1):
                                print('L')  
                        else:
                                print('N')        
        except :
            GPIO.cleanup()
            print "\r\nProgram end     "
            exit()
                                            
def originalCode():
        
        try:
                ADC = ADS1256.ADS1256()
                if (ADC.ADS1256_init() == -1):
                        exit()
                while(1):
                    
                    # t=time.time()
                        ADC_Value = ADC.ADS1256_GetAll()
                        # print "  rint " + str((time.time()-t)*1000)+" mS in reading only channel 0\n                          "
                        
                        #ADC_Value=ADC.ADS1256_GetChannalValue(0)
                        #ADC_Value=ADC_Value*5.0/0x7fffff
                        #if(ADC_Value>3):
                        #        print("HL")
                        #print ("ADC = %.5f \n"%(ADC_Value))
                        
                        
                        print ("0 ADC = %.5f"%(ADC_Value[0]*5.0/0x7fffff))
                        print ("1 ADC = %.5f"%(ADC_Value[1]*5.0/0x7fffff))
                        print ("2 ADC = %.5f"%(ADC_Value[2]*5.0/0x7fffff))
                        print ("3 ADC = %.5f"%(ADC_Value[3]*5.0/0x7fffff))
                        print ("4 ADC = %.5f"%(ADC_Value[4]*5.0/0x7fffff))
                        print ("5 ADC = %.5f"%(ADC_Value[5]*5.0/0x7fffff))
                        print ("6 ADC = %.5f"%(ADC_Value[6]*5.0/0x7fffff))
                        print ("7 ADC = %.5f"%(ADC_Value[7]*5.0/0x7fffff)) 
                        
                        # print "0 ADC = ",(ADC_Value[0])
                        # print "1 ADC = ",(ADC_Value[1])
                        # print "2 ADC = ",(ADC_Value[2])
                        # print "3 ADC = ",(ADC_Value[3])
                        # print "4 ADC = ",(ADC_Value[4])
                        # print "5 ADC = ",(ADC_Value[5])
                        # print "6 ADC = ",(ADC_Value[6])
                        # print "7 ADC = ",(ADC_Value[7])

                        print ("\33[9A")
        except :
            GPIO.cleanup()
            print "\r\nProgram end     "
            exit()
