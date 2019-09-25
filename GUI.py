#import tkinter as tk
#from Tkinter import *

from tkinter import StringVar
from tkinter import Frame	
from tkinter import Tk	
from tkinter import Button
from tkinter import Label

import time
import ADS1256
import RPi.GPIO as GPIO
	
class Application(Frame):
	

		
		
	def __init__(self, master=None):
		
		self.master=master
		self.master.title("Tag Tester")
		self.master.geometry("400x350")
		
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
		self.b1.grid(row=y, column=x, pady=3)
		
		x=0
		y=1
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
		y=2
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
		y=2	
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
		y=2				
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
		y=2	
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
		self.exit.grid(row=y, column=1)
			 
				 


	


			
			
			
	def startTest(self): 
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
				
		ADC_values=read_ADC()
		count=0
		for x in ADC_values:
				
			ADC_values[count]=round(ADC_values[count]*5.0/0x7fffff,2)
			#print(ADC_values[count])
			count=count+1 
			
		self.currentAction.set("Reading Values")
				
		self.vbatt.set(str(ADC_values[0])+" V")
		self.vcoil.set(str(ADC_values[1])+" V")
		self.vmcu.set(str(ADC_values[2])+" V")
		self.vreg.set(str(ADC_values[3])+" V")

			
		#Vbatt
		if ADC_values[0]>3 and ADC_values[0] < 4.2:
			self.llll1.config(bg="green")
		else:
			self.llll1.config(bg="red")
				
		#Vcoil			
		if ADC_values[0]>4.9 and ADC_values[0] < 5.1:
			self.llll2.config(bg="green")
		else:
			self.llll2.config(bg="red")	
				
		#Vmcu			
		if ADC_values[0]>3.2 and ADC_values[0] < 3.4:
			self.llll3.config(bg="green")
		else:
			self.llll3.config(bg="red")	
				
		#Vreg			
		if ADC_values[0]>1.7 and ADC_values[0] < 1.9:
			self.llll4.config(bg="green")
		else:
			self.llll4.config(bg="red")	
			

		#PF6 LED low					
		self.currentAction.set("Reading PF6 LED LOW")
		self.master.update()
		time.sleep(self.waitdelay)
		self.led_low.set(str(ADC_values[4])+" V")
		if ADC_values[0]>0 and ADC_values[0] < 0.5:
			self.llll5.config(bg="green")
		else:
			self.llll5.config(bg="red")
			  
		  
		
		

			
		#PF6 LED high
		self.currentAction.set("Reading PF6 LED HIGH")
		self.master.update()
		time.sleep(self.waitdelay)
		self.led_high.set(str(ADC_values[4])+" V")			
		if ADC_values[0]>2.7 and ADC_values[0] < 5.1:
			self.llll6.config(bg="green")
		else:
			self.llll6.config(bg="red")	
			
		#PC10 vbatt sense low
		self.currentAction.set("Reading PC10 vbatt sense LOW")
		self.master.update()
		time.sleep(self.waitdelay)
		self.vbatt_sense_low.set(str(ADC_values[5])+" V")			
		if ADC_values[0]>0 and ADC_values[0] < 0.5:
			self.llll7.config(bg="green")
		else:
			self.llll7.config(bg="red")			
			
		#PC10 vbatt sense high	
		self.currentAction.set("Reading PC10 vbatt sense HIGH")
		self.master.update()
		time.sleep(self.waitdelay)
		self.vbatt_sense_high.set(str(ADC_values[5])+" V")		
		if ADC_values[0]>2.7 and ADC_values[0] < 5.1:
			self.llll8.config(bg="green")
		else:
			self.llll8.config(bg="red")	
			
		#PA4 bleeding low
		self.currentAction.set("Reading PA4 bleeding LOW")
		self.master.update()
		time.sleep(self.waitdelay)
		self.bleeding_low.set(str(ADC_values[6])+" V")			
		if ADC_values[0]>0 and ADC_values[0] < 0.5:
			self.llll9.config(bg="green")
		else:
			self.llll9.config(bg="red")
			
		#PA4 bleeding high			
		self.currentAction.set("Reading PA4 bleeding HIGH")
		self.master.update()
		time.sleep(self.waitdelay)
		self.bleeding_high.set(str(ADC_values[6])+" V")	
		if ADC_values[0]>2.7 and ADC_values[0] < 5.1:
			self.llll10.config(bg="green")
		else:
			self.llll10.config(bg="red")		
		self.currentAction.set("Test Complete")				
		
		
def read_ADC():
	try:
		ADC = ADS1256.ADS1256()			
		if (ADC.ADS1256_init() == -1):
			pass
		 
		else:        
			return ADC.ADS1256_GetAll()
	except:
		GPIO.cleanup()
		print ("\r\nProgram end     ")
		
		
		
