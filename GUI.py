#import tkinter as tk
#from Tkinter import *

from tkinter import StringVar
from tkinter import Frame	
from tkinter import Tk	
from tkinter import Button
from tkinter import Label
from tkinter import W

	
class Application(Frame):
	

		
		
	def __init__(self, master=None):
		
		self.master=master
		self.master.title("Tag Tester")
		self.master.geometry("300x450")
		
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
		
		self.vbatt.set("0")
		self.vcoil.set("1")
		self.vmcu.set("2")
		self.vreg.set("3")
		self.led_low.set("4")
		self.led_high.set("5")	
		self.vbatt_sense_low.set("6")
		self.vbatt_sense_high.set("7")
		self.bleeding_low.set("8")	
		self.bleeding_high.set("9")	
				
				 
	
		x=1
		y=0
		self.b1=Button(self.master,  text="Start Test", command=self.startTest)#.pack()#(side="top",pady=30)
		self.b1.grid(row=y, column=x)
		
		
		#First column
		self.l1=Label(self.master, text="vbatt ")
		self.l2=Label(self.master, text="vcoil")
		self.l3=Label(self.master, text="vmcu")
		self.l4=Label(self.master, text="led low")
		self.l5=Label(self.master, text="led high")
		self.l6=Label(self.master, text="vbatt sense low")
		self.l7=Label(self.master, text="vbatt sense high")
		self.l8=Label(self.master, text="bleeding low")
		self.l9=Label(self.master, text="bleeding high")
		
		x=0
		y=1				
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
		
		
		#Second column
		self.ll1=Label(self.master, textvariable=self.vbatt)	
		self.ll2=Label(self.master, textvariable=self.vcoil)
		self.ll3=Label(self.master, textvariable=self.vreg)
		self.ll4=Label(self.master, textvariable=self.led_low)	
		self.ll5=Label(self.master, textvariable=self.led_high)
		self.ll6=Label(self.master, textvariable=self.vbatt_sense_low)		
		self.ll7=Label(self.master, textvariable=self.vbatt_sense_high)	
		self.ll8=Label(self.master, textvariable=self.bleeding_low)
		self.ll9=Label(self.master, textvariable=self.bleeding_high)		
		
		
		x=1
		y=1				
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
		
		
		#Third column
		self.lll1=Label(self.master, text="       ", bg= "white")
		self.lll2=Label(self.master, text="       ", bg= "white")
		self.lll3=Label(self.master, text="       ", bg= "white")
		self.lll4=Label(self.master, text="       ", bg= "white")
		self.lll5=Label(self.master, text="       ", bg= "white")
		self.lll6=Label(self.master, text="       ", bg= "white")
		self.lll7=Label(self.master, text="       ", bg= "white")
		self.lll8=Label(self.master, text="       ", bg= "white")
		self.lll9=Label(self.master, text="       ", bg= "white")
		
		x=2
		y=1	
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
		self.exit=Button(self.master,  text="Exit", bg= "red",command=self.master.destroy)#.pack(side="top",pady=40)		
		self.exit.grid(row=y, column=1)
			 
				 

	def startTest(self): 
		 
		
		self.vbatt.set("tested")
		self.vcoil.set("tested")
		self.vmcu.set("tested")
		self.vreg.set("tested")
		self.led_low.set("tested")
		self.led_high.set("tested")
		self.vbatt_sense_low.set("tested")
		self.vbatt_sense_high.set("tested")
		self.bleeding_low.set("tested")
		self.bleeding_high.set("tested")
		
		self.lll1.config(bg="red")
		self.lll2.config(bg="red")		
		self.lll3.config(bg="red")		
		self.lll4.config(bg="red")
		self.lll5.config(bg="red")		
		self.lll6.config(bg="red")		
		self.lll7.config(bg="red")
		self.lll8.config(bg="red")		
		self.lll9.config(bg="red")			
		
		
		
		
        
