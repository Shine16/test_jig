#import tkinter as tk
#from Tkinter import *

from tkinter import StringVar
from tkinter import Frame       
from tkinter import Tk  
from tkinter import Button
from tkinter import Label
from tkinter import Entry

import time
import ADS1256
import RPi.GPIO as GPIO
import os
import sys
        
class Application(Frame):       
                
        def __init__(self, master=None):
                
                self.master=master
                self.master.title("Tag Tester")
                self.master.geometry("480x450")
                
                self.vbatt=StringVar()
                self.vcoil=StringVar()
                self.vmcu=StringVar()
                self.vreg=StringVar()
                self.led_low=StringVar()
                self.led_high=StringVar()
                self.vbatt_sense_low=StringVar()
                self.vbatt_sense_high=StringVar()
                self.bleeding_low=StringVar()
                self.bleeding_high=StringVar()  
                self.currentAction=StringVar()
                
                self.vbatt.set("0 V")
                self.vcoil.set("0 V")
                self.vmcu.set("0 V")
                self.vreg.set("0 V")
                self.led_low.set("0 V")
                self.led_high.set("0 V")        
                self.vbatt_sense_low.set("0 V")
                self.vbatt_sense_high.set("0 V")
                self.bleeding_low.set("0 V")    
                self.bleeding_high.set("0 V")   
                                
                self.currentAction.set("Press Start Test to begin")              
        
                x=1
                y=0
                self.b1=Button(self.master,  text="Start Test", command=self.startTest)
                self.b1.grid(row=y, column=x, pady=5)
                
                x=0
                y=1             
                self.el1=Label(self.master, text="Serial Number")
                self.el1.grid(row=y, column=x,pady=5)
                
                x=1
                self.e1=Entry(self.master)
                self.e1.grid(row=y, column=x)#, pady=3)
                
                tabley=3
                
                
                x=0
                y=2
                self.d1=Label(self.master, textvariable=self.currentAction)
                self.d1.grid(row=y, column=x, columnspan=4, pady=8)
                                
                #First column
                self.l0=Label(self.master, text="SIGNAL")
                self.l1=Label(self.master, text="Vbatt ")
                self.l2=Label(self.master, text="Vcoil")
                self.l3=Label(self.master, text="Vmcu")
                self.l4=Label(self.master, text="Vreg")
                self.l5=Label(self.master, text="PF6 led low")
                self.l6=Label(self.master, text="PF6 led high")
                self.l7=Label(self.master, text="PC10 vbatt sense low")
                self.l8=Label(self.master, text="PC10 vbatt sense high")
                self.l9=Label(self.master, text="PA4 bleeding low")
                self.l10=Label(self.master, text="PA4 bleeding high")
                
                x=0
                y=tabley
                self.l0.grid(row=y, column=x)
                y+=1                    
                self.l1.grid(row=y, column=x)
                y+=1
                self.l2.grid(row=y, column=x)
                y+=1
                self.l3.grid(row=y, column=x)
                y+=1
                self.l4.grid(row=y, column=x)
                y+=1
                self.l5.grid(row=y, column=x)
                y+=1
                self.l6.grid(row=y, column=x)                                                   
                y+=1
                self.l7.grid(row=y, column=x)
                y+=1
                self.l8.grid(row=y, column=x)
                y+=1
                self.l9.grid(row=y, column=x)           
                y+=1
                self.l10.grid(row=y, column=x)
                
                #Second column
                self.ll0=Label(self.master, text="Pass Criteria")
                self.ll1=Label(self.master, text="3.0-4.2 V")
                self.ll2=Label(self.master, text="4.9-5.1 V")
                self.ll3=Label(self.master, text="3.2-3.4 V")
                self.ll4=Label(self.master, text="1.7-1.9 V")
                self.ll5=Label(self.master, text="<500 mV")
                self.ll6=Label(self.master, text=">2.7 V")
                self.ll7=Label(self.master, text="<500 mV")
                self.ll8=Label(self.master, text=">2.7 V")
                self.ll9=Label(self.master, text="<500 mV")
                self.ll10=Label(self.master, text=">2.7 V")
                
                x=1
                y=tabley
                self.ll0.grid(row=y, column=x)
                y+=1                    
                self.ll1.grid(row=y, column=x)
                y+=1
                self.ll2.grid(row=y, column=x)
                y+=1
                self.ll3.grid(row=y, column=x)
                y+=1
                self.ll4.grid(row=y, column=x)
                y+=1
                self.ll5.grid(row=y, column=x)
                y+=1
                self.ll6.grid(row=y, column=x)                                                  
                y+=1
                self.ll7.grid(row=y, column=x)
                y+=1
                self.ll8.grid(row=y, column=x)
                y+=1
                self.ll9.grid(row=y, column=x)          
                y+=1
                self.ll10.grid(row=y, column=x)                 
                
                #Third column
                self.lll0=Label(self.master, text="Actual Value")
                self.lll1=Label(self.master, textvariable=self.vbatt)   
                self.lll2=Label(self.master, textvariable=self.vcoil)
                self.lll3=Label(self.master, textvariable=self.vmcu)
                self.lll4=Label(self.master, textvariable=self.vreg)
                self.lll5=Label(self.master, textvariable=self.led_low) 
                self.lll6=Label(self.master, textvariable=self.led_high)
                self.lll7=Label(self.master, textvariable=self.vbatt_sense_low)         
                self.lll8=Label(self.master, textvariable=self.vbatt_sense_high)        
                self.lll9=Label(self.master, textvariable=self.bleeding_low)
                self.lll10=Label(self.master, textvariable=self.bleeding_high)          
                
                
                x=2
                y=tabley                                
                self.lll0.grid(row=y, column=x)
                y+=1
                self.lll1.grid(row=y, column=x)
                y+=1
                self.lll2.grid(row=y, column=x)
                y+=1
                self.lll3.grid(row=y, column=x)
                y+=1
                self.lll4.grid(row=y, column=x)
                y+=1
                self.lll5.grid(row=y, column=x)
                y+=1
                self.lll6.grid(row=y, column=x)                                                 
                y+=1
                self.lll7.grid(row=y, column=x)
                y+=1
                self.lll8.grid(row=y, column=x)
                y+=1
                self.lll9.grid(row=y, column=x) 
                y+=1
                self.lll10.grid(row=y, column=x)                        
                
                #Fourth column
                self.llll0=Label(self.master, text="Pass / Fail")
                self.llll1=Label(self.master, text="       ", bg= "white")
                self.llll2=Label(self.master, text="       ", bg= "white")
                self.llll3=Label(self.master, text="       ", bg= "white")
                self.llll4=Label(self.master, text="       ", bg= "white")
                self.llll5=Label(self.master, text="       ", bg= "white")
                self.llll6=Label(self.master, text="       ", bg= "white")
                self.llll7=Label(self.master, text="       ", bg= "white")
                self.llll8=Label(self.master, text="       ", bg= "white")
                self.llll9=Label(self.master, text="       ", bg= "white")
                self.llll10=Label(self.master, text="       ", bg= "white")
                
                x=3
                y=tabley        
                self.llll0.grid(row=y, column=x)
                y+=1
                self.llll1.grid(row=y, column=x)
                y+=1
                self.llll2.grid(row=y, column=x)
                y+=1
                self.llll3.grid(row=y, column=x)
                y+=1
                self.llll4.grid(row=y, column=x)
                y+=1
                self.llll5.grid(row=y, column=x)
                y+=1
                self.llll6.grid(row=y, column=x)                                                        
                y+=1
                self.llll7.grid(row=y, column=x)
                y+=1
                self.llll8.grid(row=y, column=x)
                y+=1
                self.llll9.grid(row=y, column=x)        
                y+=1
                self.llll10.grid(row=y, column=x)
                                

                y+=2            
                self.exit=Button(self.master,  text="Exit",command=self.master.destroy)#.pack(side="top",pady=40)               
                self.exit.grid(row=y, column=1,pady=10)
                         
                                 


        


                        
                        
                        
        def startTest(self): 
                
                #make test report directory if not exist
                try:
                        os.mkdir('test reports')
                except FileExistsError:
                        pass
                
         
                serial_number=self.e1.get()

                test_Report=open(str(os.path.dirname(__file__))+"/test reports/"+serial_number+".txt","a")
                test_Report.write("Tag Test Report\n")
                test_Report.write("Serial Number:\t\t"+str(serial_number)+"\n")
                test_Report.write("Time:\t\t\t"+str(time.asctime())+"\n\n")
                
                
                self.waitdelay = 0.5#1
                
                self.vbatt.set("0 V")
                self.vcoil.set("0 V")
                self.vmcu.set("0 V")
                self.vreg.set("0 V")
                self.led_low.set("0 V")
                self.led_high.set("0 V")        
                self.vbatt_sense_low.set("0 V")
                self.vbatt_sense_high.set("0 V")
                self.bleeding_low.set("0 V")    
                self.bleeding_high.set("0 V")
                
                self.llll1.config(bg="white")
                self.llll2.config(bg="white")
                self.llll3.config(bg="white")
                self.llll4.config(bg="white")           
                self.llll5.config(bg="white")
                self.llll6.config(bg="white")
                self.llll7.config(bg="white")
                self.llll8.config(bg="white")           
                self.llll9.config(bg="white")
                self.llll10.config(bg="white")
                                                
                self.currentAction.set("Reading Values")
                self.master.update()
                time.sleep(1)
                                
                ADC_values=self.read_ADC()
                
                        
                self.currentAction.set("Reading Values")
                                
                self.vbatt.set(str(ADC_values[0])+" V")
                self.vcoil.set(str(ADC_values[1])+" V")
                self.vmcu.set(str(ADC_values[2])+" V")
                self.vreg.set(str(ADC_values[3])+" V")          

                
                #Vbatt
                test_Report.write("Vbatt:\t\t\t"+str(ADC_values[0])+" V\t")
                if ADC_values[0]>3 and ADC_values[0] < 4.2:
                        self.llll1.config(bg="green")
                        test_Report.write("pass\n")
                else:
                        self.llll1.config(bg="red")
                        test_Report.write("fail\n")
                                
                #Vcoil  
                test_Report.write("Vcoil:\t\t\t"+str(ADC_values[1])+" V\t")             
                if ADC_values[1]>4.9 and ADC_values[1] < 5.1:
                        self.llll2.config(bg="green")
                        test_Report.write("pass\n")
                else:
                        self.llll2.config(bg="red")     
                        test_Report.write("fail\n")
                                
                #Vmcu                   
                test_Report.write("Vmcu:\t\t\t"+str(ADC_values[2])+" V\t")
                if ADC_values[2]>3.2 and ADC_values[2] < 3.4:
                        self.llll3.config(bg="green")
                        test_Report.write("pass\n")
                else:
                        self.llll3.config(bg="red")     
                        test_Report.write("fail\n")
                                
                #Vreg                   
                test_Report.write("Vreg:\t\t\t"+str(ADC_values[3])+" V\t")
                if ADC_values[3]>1.7 and ADC_values[3] < 1.9:
                        self.llll4.config(bg="green")
                        test_Report.write("pass\n")
                else:
                        self.llll4.config(bg="red")     
                        test_Report.write("fail\n")
                        

                
                samples=20
                time_to_sample=1
                
                
                
                
                
                #PF6 LED low    
                self.currentAction.set("Reading PF6 LED low")
                self.master.update()

                ADC_values[4] , testpass =self.read_sampleADC(4, 0 , 0.5)#sport,low,high range 
                test_Report.write("PF6 LED Low:\t\t"+str(ADC_values[4])+" V\t")
                
                self.led_low.set(str(ADC_values[4])+" V")
                
                if testpass:
                        self.llll5.config(bg="green")
                        test_Report.write("pass\n")
                else:
                        self.llll5.config(bg="red")
                        test_Report.write("fail\n") 
                
                

                        
                #PF6 LED high
                #ADC_values[4]=self.read_sampleADC(4,samples,time_to_sample)
                self.currentAction.set("Reading PF6 LED high")
                self.master.update()

                ADC_values[4] , testpass =self.read_sampleADC(4, 2.7 , 5.1 )
                test_Report.write("PF6 LED High:\t\t"+str(ADC_values[4])+" V\t")
                
                self.led_high.set(str(ADC_values[4])+" V")
                
                if testpass:
                        self.llll6.config(bg="green")
                        test_Report.write("pass\n")
                else:
                        self.llll6.config(bg="red")     
                        test_Report.write("fail\n")
                 
                        
                        
                #PC10 vbatt sense low
                #ADC_values[5]=self.read_sampleADC(5,samples,time_to_sample)
                self.currentAction.set("Reading PC10 vbatt sense LOW")
                self.master.update()
                
                ADC_values[5] , testpass =self.read_sampleADC(5, 0 , 0.5 ) 
                test_Report.write("PC10 vbatt sense low:\t"+str(ADC_values[5])+" V\t") 
                
                self.vbatt_sense_low.set(str(ADC_values[5])+" V")                       
                if testpass:
                        self.llll7.config(bg="green")
                        test_Report.write("pass\n")
                else:
                        self.llll7.config(bg="red")                     
                        test_Report.write("fail\n")

                        
                #PC10 vbatt sense high  
                #ADC_values[5]=self.read_sampleADC(5,samples,time_to_sample)
                self.currentAction.set("Reading PC10 vbatt sense HIGH")
                self.master.update()
                
                ADC_values[5] , testpass =self.read_sampleADC(5, 2.7 , 5.1 )

                test_Report.write("PC10 vbatt sense high:\t"+str(ADC_values[5])+" V\t") 
                self.vbatt_sense_high.set(str(ADC_values[5])+" V")
                
                if ADC_values[5]>2.7 and ADC_values[5] <= 5.1:
                        self.llll8.config(bg="green")
                        test_Report.write("pass\n")
                else:
                        self.llll8.config(bg="red")     
                        test_Report.write("fail\n")
                
                        
                #PA4 bleeding low
                #ADC_values[6]=self.read_sampleADC(6,samples,time_to_sample)
                self.currentAction.set("Reading PA4 bleeding LOW")
                self.master.update()
                
                ADC_values[6],testpass=self.read_sampleADC(6, 0 , 0.5 )
                
                test_Report.write("PA4 bleeding low:\t"+str(ADC_values[6])+" V\t") 
                self.bleeding_low.set(str(ADC_values[6])+" V")
                
                if testpass:
                        self.llll9.config(bg="green")
                        test_Report.write("pass\n")
                else:
                        self.llll9.config(bg="red")
                        test_Report.write("fail\n")
                 
                        
                #PA4 bleeding high      
                #ADC_values[6]=self.read_sampleADC(6,samples,time_to_sample)
                self.currentAction.set("Reading PA4 bleeding HIGH")
                self.master.update()
                
                ADC_values[6],testpass=self.read_sampleADC(6, 2.7 , 5.1 )
                
                test_Report.write("PA4 bleeding high:\t"+str(ADC_values[6])+" V\t")             
                self.bleeding_high.set(str(ADC_values[6])+" V")
                
                if testpass:
                        self.llll10.config(bg="green")
                        test_Report.write("pass\n")
                else:
                        self.llll10.config(bg="red")            
                        test_Report.write("fail\n")
                
                
                self.currentAction.set("Test Complete") 
                
                test_Report.close()
                        
                
                
                
                
        def read_ADC(self):
                try:
                        ADC = ADS1256.ADS1256()                 
                        if (ADC.ADS1256_init() == -1):
                                pass
                         
                        else:        
                                ADC_read=ADC.ADS1256_GetAll()
                                count=0
                                for x in ADC_read:                                      
                                        ADC_read[count]=round(ADC_read[count]*5.0/0x7fffff,2)
                                        count=count+1 
                                return ADC_read
                                
                except:
                        GPIO.cleanup()
                        print ("\r\nProgram end     ")
                        
                        
        def read_singleADC(self,port):
                try:
                        ADC = ADS1256.ADS1256()
                        print(time.asctime())
                        return round(ADC.ADS1256_GetChannalValue(port)*5.0/0x7fffff,2)
                        
                except:
                        GPIO.cleanup()
                        print ("\r\nProgram end     ")          
                        
                        
                        
        def read_sampleADC(self , port, low , high ):
                
                listofSamples=[]
                
                try:
                        oldtime=time.time()
                        sampletime=0.05
                        low=float(low)
                        high=float(high)                        
                                                        
                        ADC = ADS1256.ADS1256()
                        print("reading samples on port "+str(port))
        
                        count=0
                        while count<60 and len(listofSamples) < 10:
                                count+=1
                                reading=round(ADC.ADS1256_GetChannalValue(port)*5.0/0x7fffff,2)
                
                                if reading>=low and reading<=high:                
                                    listofSamples.append(reading)
                                time.sleep(sampletime)
                                
                        
                        print(count)
                        print(listofSamples)
                                         
                        print(time.time()-oldtime)
                        if(len(listofSamples)>=10):
                                listofSamples.sort()
                                print("success")
                                return listofSamples[4],1
                        else:
                                print("not success")
                                return round(ADC.ADS1256_GetChannalValue(port)*5.0/0x7fffff,2),0
                 
                        
                                
                        
                except:
                        GPIO.cleanup()
                        print ("\r\nERROR IN READ  ")                
                
                        
                
