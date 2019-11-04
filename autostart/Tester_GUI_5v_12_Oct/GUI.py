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
import threading

import currentsense
        
class Application(Frame):       

        def __init__(self, master=None):
                """

                This will create the window, labels and buttons required.
                
                """
                self.master=master
                self.master.title("Tag Tester")
                self.master.geometry("480x570")
                
                self.vbatt=StringVar()
                self.vmcu=StringVar()
                self.vreg=StringVar()
                self.led_low=StringVar()
                self.led_high=StringVar()
                self.vbatt_sense_low=StringVar()
                self.vbatt_sense_high=StringVar()
                self.bleeding_low=StringVar()
                self.bleeding_high=StringVar()  
                self.currentAction=StringVar()
                self.reset_time=StringVar()
                self.vbatt2=StringVar()
                self.cnew=StringVar() 
                self.cprog=StringVar()
                self.ccharge=StringVar()
                self.vcoil=StringVar()
                
                self.vbatt.set("0 V")                
                self.vmcu.set("0 V")
                self.vreg.set("0 V")
                self.led_low.set("0 V")
                self.led_high.set("0 V")        
                self.vbatt_sense_low.set("0 V")
                self.vbatt_sense_high.set("0 V")
                self.bleeding_low.set("0 V")    
                self.bleeding_high.set("0 V")   
                self.reset_time.set("0 mS")
                self.vcoil.set("0 V")
                self.vbatt2.set("0 V")
                self.cnew.set("0 mA")
                self.cprog.set("0 mA")
                self.ccharge.set("0 mA")
               
                                
                self.currentAction.set("Press Start Test to begin")              
                
                
                #Serial number entry
                x=0
                y=0            
                self.el1=Label(self.master, text="Serial Number")
                self.el1.grid(row=y, column=x,pady=5)
                                
                x=1
                self.e1=Entry(self.master)
                self.e1.grid(row=y, column=x)
                
                
               
                
                
                #read current button
                x=1
                y=1                
                self.b1=Button(self.master,  text="Read initial current", command=self.readcurrent)
                self.b1.grid(row=y, column=x, pady=10)
                
                
                #current reading display
                x=0
                y=2
                self.l13=Label(self.master, text="Current new")
                self.l13.grid(row=y, column=x)
                
                x=1
                self.ll13=Label(self.master, text=" ")
                self.ll13.grid(row=y, column=x)
                
                x=2                
                self.lll13=Label(self.master, textvariable=self.cnew)
                self.lll13.grid(row=y, column=x)
                
                #start test button
                x=1
                y=3
                self.b1=Button(self.master,  text="Start Test", command=self.startTest)
                self.b1.grid(row=y, column=x, pady=10)
                                
                x=0
                y=4
                self.d1=Label(self.master, textvariable=self.currentAction)
                self.d1.grid(row=y, column=x, columnspan=4, pady=8)
                
                tabley=5
                                
                #First column
                self.l0=Label(self.master, text="SIGNAL")
                self.l1=Label(self.master, text="Vbatt ")
                self.l2=Label(self.master, text="Vmcu")
                self.l3=Label(self.master, text="Vreg")
                self.l4=Label(self.master, text="PF6 led low")
                self.l5=Label(self.master, text="PF6 led high")
                self.l6=Label(self.master, text="PC10 vbatt sense low")
                self.l7=Label(self.master, text="PC10 vbatt sense high")
                self.l8=Label(self.master, text="PA4 bleeding low")
                self.l9=Label(self.master, text="PA4 bleeding high")
                self.l10=Label(self.master, text="Reset timing")
                self.l11=Label(self.master, text="Vcoil")
                self.l12=Label(self.master, text="Charging Voltage")                
                
                self.l14=Label(self.master, text="Current programmed")
                self.l15=Label(self.master, text="Current charging")
                
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
                y+=1
                self.l11.grid(row=y, column=x)                
                y+=1
                self.l12.grid(row=y, column=x)                
                y+=1
                self.l14.grid(row=y, column=x)
                y+=1
                self.l15.grid(row=y, column=x)
                
                #Second column
                self.ll0=Label(self.master, text="Pass Criteria")
                self.ll1=Label(self.master, text="3.0-4.2 V")
                self.ll2=Label(self.master, text="3.2-3.4 V")
                self.ll3=Label(self.master, text="1.7-1.9 V")
                self.ll4=Label(self.master, text="<500 mV")
                self.ll5=Label(self.master, text=">2.7 V")
                self.ll6=Label(self.master, text="<500 mV")
                self.ll7=Label(self.master, text=">2.7 V")
                self.ll8=Label(self.master, text="<500 mV")
                self.ll9=Label(self.master, text=">2.7 V")
                self.ll10=Label(self.master, text=">5 mS")
                self.ll11=Label(self.master, text="4.9-5.1 V")
                self.ll12=Label(self.master, text="4.0-4.2 V")
        
                
                self.ll14=Label(self.master, text=" ")
                self.ll15=Label(self.master, text=" ")
                
                x=1
                y=tabley
                self.ll0.grid(row=y, column=x)
                y+=1                    
                self.ll1.grid(row=y, column=x)
                y+=1
                self.ll2.grid(row=y, column=x)#Vcoil
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
                y+=1
                self.ll11.grid(row=y, column=x)                
                y+=1
                self.ll12.grid(row=y, column=x)                                
                
                y+=1
                self.ll14.grid(row=y, column=x)
                y+=1
                self.ll15.grid(row=y, column=x)
                
                
                #Third column
                self.lll0=Label(self.master, text="Actual Value")
                self.lll1=Label(self.master, textvariable=self.vbatt)                   
                self.lll2=Label(self.master, textvariable=self.vmcu)
                self.lll3=Label(self.master, textvariable=self.vreg)
                self.lll4=Label(self.master, textvariable=self.led_low) 
                self.lll5=Label(self.master, textvariable=self.led_high)
                self.lll6=Label(self.master, textvariable=self.vbatt_sense_low)         
                self.lll7=Label(self.master, textvariable=self.vbatt_sense_high)        
                self.lll8=Label(self.master, textvariable=self.bleeding_low)
                self.lll9=Label(self.master, textvariable=self.bleeding_high)          
                self.lll10=Label(self.master, textvariable=self.reset_time)
                self.lll11=Label(self.master, textvariable=self.vcoil)
                self.lll12=Label(self.master, textvariable=self.vbatt2)  
                
                 
                self.lll14=Label(self.master, textvariable=self.cprog) 
                self.lll15=Label(self.master, textvariable=self.ccharge) 
                
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
                y+=1
                self.lll11.grid(row=y, column=x)                
                y+=1
                self.lll12.grid(row=y, column=x)                
                
                y+=1
                self.lll14.grid(row=y, column=x)
                y+=1
                self.lll15.grid(row=y, column=x)
                
                
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
                self.llll11=Label(self.master, text="       ", bg= "white")                
                self.llll12=Label(self.master, text="       ", bg= "white")
                
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
                y+=1
                self.llll11.grid(row=y, column=x)                    
                y+=1
                self.llll12.grid(row=y, column=x)                            
                
                
                y+=6           
                self.exit=Button(self.master,  text="Exit",command=self.master.destroy)#.pack(side="top",pady=40)               
                self.exit.grid(row=y, column=1,pady=10)
                
                
                       
                                 


        
        def readcurrent(self):
                
                serial_number=self.e1.get()
                
                #toggle wireless charger and connect batt
                relaywirelesscharge = 24
                relaybatt = 23
                GPIO.setmode(GPIO.BCM)             
                GPIO.setup(relaywirelesscharge, GPIO.OUT)  
                GPIO.setup(relaybatt          , GPIO.OUT)  
                
                GPIO.output(relaybatt          , GPIO.HIGH) #battery
                GPIO.output(relaywirelesscharge, GPIO.HIGH) #wireless charger
                time.sleep(2)
                GPIO.output(relaywirelesscharge, GPIO.LOW)   
                time.sleep(2)             
                
                
                test_Report=open(str(os.path.dirname(__file__))+"/test reports/"+serial_number+".txt","a")
                test_Report.write("Tag Initial Current Reading\n")
                test_Report.write("Serial Number:\t\t"+str(serial_number)+"\n")
                test_Report.write("Time:\t\t\t"+str(time.asctime())+"\n")
                
                initialcurrent = currentsense.currentRead()
                initialcurrent = '{:.2f}'.format(initialcurrent.currentReading())+" mA"
                print(initialcurrent)
                self.cnew.set(initialcurrent)                
                test_Report.write("Initial Current:\t"+str(initialcurrent))                
                test_Report.write("\n\n\n")
                
                test_Report.close()
                        
                        
                        
        def startTest(self):
                
                """

                Function to start test procedures.
                Vbatt at port 0
                Vmcu  at port 2
                Vreg  at port 3

                PF6 led high and low      at port 4
                PC10 vbatt sense high low at port 5
                PA4 bleeding high low     at port 6
                Vcoil                     at port 1

                A relay to power on wireless charger at GPIO24
                and GPIO27
        
                """
                
                #make test report directory if not exist
                try:
                        os.mkdir('test reports')
                except FileExistsError:
                        pass
                
                resetsense=27
                relaywirelesscharge = 24
                relaybatt = 23
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(relaywirelesscharge, GPIO.OUT)  
                GPIO.setup(relaybatt          , GPIO.OUT) 
                GPIO.setup(resetsense          , GPIO.IN) 
                                
                GPIO.output(relaywirelesscharge, GPIO.LOW)  
                GPIO.output(relaybatt          , GPIO.LOW)
                                
                serial_number=self.e1.get()

                test_Report=open(str(os.path.dirname(__file__))+"/test reports/"+serial_number+".txt","a")
                test_Report.write("Tag Test Report\n")
                test_Report.write("Serial Number:\t\t"+str(serial_number)+"\n")
                test_Report.write("Time:\t\t\t"+str(time.asctime())+"\n\n")

          
                        
                self.waitdelay = 0.5
                
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
                self.reset_time.set("0 mS")
                self.vbatt2.set("0 V")
                
                #self.cnew.set("0 mA")
                self.cprog.set("0 mA")
                self.ccharge.set("0 mA")
                
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
                self.llll11.config(bg="white")
                self.llll12.config(bg="white")
                                
                GPIO.output(relaybatt          , GPIO.HIGH) #battery
                GPIO.output(relaywirelesscharge, GPIO.HIGH) #wireless charger
                time.sleep(2)
                GPIO.output(relaywirelesscharge, GPIO.LOW)
                self.currentAction.set("Reading Values")
                self.master.update()
                time.sleep(3)
                                
                ADC_values=self.read_ADC()
                
                        
                self.currentAction.set("Reading Vbatt")  
                        
                
                
                #Vbatt
                ADC_values[0] , testpass =self.read_sampleADC(0 , 3 , 4.2)
                vbattf='{:.2f}'.format(ADC_values[0])
                self.vbatt.set(vbattf+" V")   
                
                test_Report.write("Vbatt:\t\t\t"+vbattf+" V\t")
                if testpass:
                        self.llll1.config(bg="green")
                        test_Report.write("pass\n")
                else:
                        self.llll1.config(bg="red")     
                        test_Report.write("fail\n")
                self.master.update()
                
                self.currentAction.set("Reading Current")                               
                programcurrent = currentsense.currentRead()
                programcurrent = '{:.2f}'.format(programcurrent.currentReading())+" mA"
                print(programcurrent)
                self.cprog.set(programcurrent)                
                
                
                #Vmcu 
                ADC_values[2] , testpass =self.read_sampleADC(2 , 3.2 , 3.4)
                vmcuf='{:.2f}'.format(ADC_values[2])
                self.vmcu.set(vmcuf+" V")
                
                test_Report.write("Vmcu:\t\t\t"+vmcuf+" V\t")
                if testpass:
                        self.llll2.config(bg="green")
                        test_Report.write("pass\n")
                else:
                        self.llll2.config(bg="red")     
                        test_Report.write("fail\n")
                self.master.update()
                
                #Vreg 
                ADC_values[3] , testpass =self.read_sampleADC(3 , 1.7 , 1.9)
                vregf='{:.2f}'.format(ADC_values[3])
                self.vreg.set(vregf+" V")
                
                test_Report.write("Vreg:\t\t\t"+vregf+" V\t")
                self.master.update()

                if testpass:
                        self.llll3.config(bg="green")
                        test_Report.write("pass\n")
                else:
                        self.llll3.config(bg="red")     
                        test_Report.write("fail\n")
                self.master.update()
        

                ################# Sample on ports 3-6 ########################
                samples=20
                time_to_sample=1
                
                
                
                
                
                #PF6 LED low    
                self.currentAction.set("Reading PF6 LED low")
                self.master.update()

                ADC_values[4] , testpass =self.read_sampleADC(4, 0 , 0.5)#sport,low,high range 
                ledlf = '{:.2f}'.format(ADC_values[4])
                
                test_Report.write("PF6 LED Low:\t\t"+ledlf+" V\t")                
                self.led_low.set(ledlf+" V")
                
                if testpass:
                        self.llll4.config(bg="green")
                        test_Report.write("pass\n")
                else:
                        self.llll4.config(bg="red")
                        test_Report.write("fail\n") 
                
                self.master.update()


                        
                #PF6 LED high
                self.currentAction.set("Reading PF6 LED high")
                self.master.update()

                ADC_values[4] , testpass =self.read_sampleADC(4, 2.7 , 5.1 )
                ledhf= '{:.2f}'.format(ADC_values[4])
                
                test_Report.write("PF6 LED High:\t\t"+ledhf+" V\t")                
                self.led_high.set(ledhf+" V")
                
                if testpass:
                        self.llll5.config(bg="green")
                        test_Report.write("pass\n")
                else:
                        self.llll5.config(bg="red")     
                        test_Report.write("fail\n")
                 
                        
                        
                #PC10 vbatt sense low
                self.currentAction.set("Reading PC10 vbatt sense LOW")
                self.master.update()
                
                ADC_values[5] , testpass =self.read_sampleADC(5, 0 , 0.5 ) 
                vbattSenself = '{:.2f}'.format(ADC_values[5])
                
                test_Report.write("PC10 vbatt sense low:\t"+vbattSenself+" V\t")                 
                self.vbatt_sense_low.set(vbattSenself+" V")                       
                
                if testpass:
                        self.llll6.config(bg="green")
                        test_Report.write("pass\n")
                else:
                        self.llll6.config(bg="red")                     
                        test_Report.write("fail\n")

                        
                #PC10 vbatt sense high  
                self.currentAction.set("Reading PC10 vbatt sense HIGH")
                self.master.update()
                
                ADC_values[5] , testpass =self.read_sampleADC(5, 2.7 , 5.1 )
                vbattSensehf = '{:.2f}'.format(ADC_values[5])
				
                test_Report.write("PC10 vbatt sense high:\t"+vbattSensehf+" V\t") 
                self.vbatt_sense_high.set(vbattSensehf+" V")
                
                if testpass:
                        self.llll7.config(bg="green")
                        test_Report.write("pass\n")
                else:
                        self.llll7.config(bg="red")     
                        test_Report.write("fail\n")
                
                        
                #PA4 bleeding low
                self.currentAction.set("Reading PA4 bleeding LOW")
                self.master.update()
                
                ADC_values[6],testpass=self.read_sampleADC(6, 0 , 0.5 )
                bleedlf ='{:.2f}'.format(ADC_values[6])
                
                test_Report.write("PA4 bleeding low:\t"+bleedlf+" V\t") 
                self.bleeding_low.set(bleedlf+" V")
                
                if testpass:
                        self.llll8.config(bg="green")
                        test_Report.write("pass\n")
                else:
                        self.llll8.config(bg="red")
                        test_Report.write("fail\n")
                 
                        
                #PA4 bleeding high 
                self.currentAction.set("Reading PA4 bleeding HIGH")
                self.master.update()
                
                ADC_values[6],testpass=self.read_sampleADC(6, 2.7 , 5.1 )
                bleedhf ='{:.2f}'.format(ADC_values[6])
                
                test_Report.write("PA4 bleeding high:\t"+bleedhf+" V\t")             
                self.bleeding_high.set(bleedhf+" V")
                
                if testpass:
                        self.llll9.config(bg="green")
                        test_Report.write("pass\n")
                else:
                        self.llll9.config(bg="red")            
                        test_Report.write("fail\n")

		################ Sense Reset Pulse #######################
                #Reset sense
                self.currentAction.set("Sense reset pulse")
                self.master.update()


                self.timetaken=0 
                self.stopthread=False

                print("starting thread")
                x=threading.Thread(target=self.reset_sense)
                x.start()
                print(threading.active_count())

                count=0
                while self.timetaken==0 and count<40:
                        time.sleep(0.1)
                        count=count+1
                        print("reset sensing")
                        
                        
                self.stopthread=True
                x.join()
                print(threading.active_count())
                


 
                 
                print(self.timetaken)
                
                self.reset_time.set(str(self.timetaken)+" mS")
                print("Reset pulse of "+str(self.timetaken)+" mS")
                
                test_Report.write("Reset pulse:\t\t"+str(self.timetaken)+" mS\t")         
       
                if self.timetaken>5.0:
                        self.llll10.config(bg="green")
                        test_Report.write("pass\n")
                else:
                        self.llll10.config(bg="red")     
                        test_Report.write("fail\n") 
                
 
                time.sleep(1)
                
                #Vcoil
                self.currentAction.set("Reading Vcoil")
                self.master.update()

                ADC_values[1],testpass=self.read_sampleADC(1, 4.9 , 5.1 )
                vcoilf ='{:.2f}'.format(ADC_values[1])
                
                self.vcoil.set(vcoilf+" V")                        

                test_Report.write("Vcoil:\t\t\t"+vcoilf+" V\t")             
                if testpass:
                        self.llll11.config(bg="green")
                        test_Report.write("pass\n")
                else:
                        self.llll11.config(bg="red")     
                        test_Report.write("fail\n")
                        
                        
                time.sleep(2)
                
                #read batt current with charger on
                self.currentAction.set("Reading Current")                               
                chargecurrent = currentsense.currentRead()
                chargecurrent= '{:.2f}'.format(chargecurrent.currentReading())+" mA"
                print(chargecurrent)
                self.ccharge.set(chargecurrent)                
                
                
                time.sleep(1)
                #turn off batt
                GPIO.output(relaybatt , GPIO.LOW)
                
                        
                #Vbatt 2
                self.currentAction.set("Reading V batt")
                self.master.update()               
                                
                ADC_values[0],testpass=self.read_sampleADC(0, 4 , 4.2 )
                vbatt2 ='{:.2f}'.format(ADC_values[0])
                
                self.vbatt2.set(vbatt2+" V")                        

                test_Report.write("Vcoil:\t\t\t"+vbatt2+" V\t")             
                if testpass:
                        self.llll12.config(bg="green")
                        test_Report.write("pass\n")
                else:
                        self.llll12.config(bg="red")     
                        test_Report.write("fail\n")
                
                self.currentAction.set("Test Complete")
                    
                test_Report.write("Charging Current:\t"+str(chargecurrent))                
                test_Report.write("\n")
                test_Report.write("Programmed Current:\t"+str(programcurrent))                
                test_Report.write("\n")
                
                
                
                test_Report.write("\n\n\n\n")
                test_Report.close()
                
                GPIO.output(relaywirelesscharge, GPIO.LOW)
                GPIO.output(relaybatt          , GPIO.LOW)
                GPIO.cleanup()

                
        def reset_sense(self):
                
                """

                To detect a 5ms low pulse when wireless charger is powered on by relay.
                Function will record time, detect LOW, and find the difference in time
                when signal becomes HIGH again.
                timeout from main function can stop function by changing self.stopthread to True.
        
                """

                
                GPIO.output(24, GPIO.HIGH)  #power to wireless charger
                
                while GPIO.input(27)==True :
                        if self.stopthread:
                                print("not detected 1")
                                break
                        
                oldtime=time.time()
                while GPIO.input(27)==False :
                        if self.stopthread:
                                print("not detected 2")
                                break
                        
                if self.stopthread==False:        
                        self.timetaken=round((time.time()-oldtime)*1000,2)
                print(self.timetaken)
                
                



                
                
                
        def read_ADC(self):


                """

                To read all ADC channels and return values in a 8 value array.
        
                """
                
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
                
                """

                To read a single ADC channels and return the value.
        
                """

                try:
                        ADC = ADS1256.ADS1256()
                        print(time.asctime())
                        return round(ADC.ADS1256_GetChannalValue(port)*5.0/0x7fffff,2)
                        
                except:
                        GPIO.cleanup()
                        print ("\r\nProgram end     ")          
                        
                        
                        
        def read_sampleADC(self , port, low , high ):

                """

                Sample an ADC channel 0.1s interval for 3 seconds.
                Stop if 10 samples fall within low and high values.
                Sort in ascending order and send 4th value in list.
        
                """

                sampletime=0.1
                samplecount=30
                
                
                try:
                        listofSamples=[]
                        oldtime=time.time()
                        
                        low=float(low)
                        high=float(high)                        
                                                        
                        ADC = ADS1256.ADS1256()
                        print("reading samples on port "+str(port))
        
                        count=0
                        while count<samplecount and len(listofSamples) < 10:
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
           
                

                        
                
