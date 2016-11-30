#!/usr/bin/python3

# homeGUI.py
# Author: Nihesh Anderson K
# 30 Sept 2016


"""
This module is used to create the GUI interface of the homepage of LoginAT app
"""

directory=""
directory2=""

import sys
from tkinter import *
import login
import cleardata
from hashlib import md5
import initaccess
import string
import os
import credentials
import autologin

masterpwd=[None,None]


def authenticate(startGUI,passwd,passentry,rootpwd):

	"""
	Authenticates the password
	"""
	global masterpwd
	masterpwd[0]=passwd.get()
	masterpwd[1]=rootpwd.get()
	with open(directory+"master.txt","r") as file:
		for line in file:
			if(initaccess.rootvalidate(masterpwd[1])):
				if(line==md5(masterpwd[0].encode()).hexdigest()):
					startGUI.destroy()
					GUIwindow()
				else:
					passentry.delete(0,END)				
					return
			else:
				label=Label(startGUI,text="X",bg="#e0ffff",fg="#FF0000",font=(None,12)).place(x=175,y=122)
				return	

def boot():

	"""
	First menu on screen. Verifies master password
	"""
	
	try:
		file=open(directory+"master.txt","r")
		file.close()
		startGUI=Tk()
		startGUI.wm_iconbitmap(bitmap="@LoginAT_logo.xbm")
		startGUI.title("Authentication")
		border=Canvas(startGUI,width=400,height=225)
		border.pack()
		border.create_rectangle(6,6,394,50,width=0, fill="#e0ffff")
		border.create_rectangle(6,56,394,219,width=0, fill="#e0ffff")	
		startGUI.geometry("400x225")
		passwd=StringVar()
		rootpwd=StringVar()
		startGUI.resizable(width=False,height=False)
		toplabel=Label(startGUI,text="Welcome to LoginAT",font=(None,14,"bold"),bg="#e0ffff").place(x=80,y=15)
		sublabel=Label(startGUI,text="Master Password",font=(None,12),bg="#e0ffff").place(x=20,y=80)
		sublabel2=Label(startGUI,text="Root Password",font=(None,12),bg="#e0ffff").place(x=20,y=120)
		passentry=Entry(startGUI,textvariable=passwd,font=(None,11),width=17,show="*")
		passentry.place(x=195,y=80)
		passentry2=Entry(startGUI,textvariable=rootpwd,font=(None,11),width=17,show="*")
		passentry2.place(x=195,y=120)
		loginButton=Button(startGUI,text="Login",padx=5,pady=5,font=(None,12),command=lambda:authenticate(startGUI,passwd,passentry,rootpwd)).place(x=170,y=170)
		startGUI.mainloop()
	
	except FileNotFoundError:
		
		try:
			initaccess.initmaster()
			file=open(directory+"master.txt","r")
			file.close()
			boot()
			
		except:
			pass			
	
def menubutton(mGUI):
		
	"""
	Defines the menubar on the top 
	"""
	
	global masterpwd

	menubar=Menu(mGUI)

	App=Menu(menubar,tearoff=0)
	App.add_command(label="Change Master Password", command=lambda:initaccess.updatemaster(masterpwd,mGUI))
	App.add_command(label="Exit", command=lambda:exit())
	menubar.add_cascade(label="Application",menu=App)	
	login=Menu(menubar,tearoff=0)

	create=Menu(login,tearoff=0)
	create.add_command(label="Facebook",command=lambda:credentials.seekfblogin(masterpwd))
	create.add_command(label="Twitter",command=lambda:credentials.seektwitterlogin(masterpwd))
	create.add_command(label="Backpack",command=lambda:credentials.seekbackpacklogin(masterpwd))
	create.add_command(label="Instagram",command=lambda:credentials.seekinstalogin(masterpwd))
	create.add_command(label="Gmail",command=lambda:credentials.seekgmaillogin(masterpwd))
	create.add_command(label="Drive",command=lambda:credentials.seekdrivelogin(masterpwd))
	create.add_command(label="Youtube",command=lambda:credentials.seekyoutubelogin(masterpwd))
	login.add_cascade(label="Add/Modify",menu=create)

	delete=Menu(login,tearoff=0)
	delete.add_command(label="Facebook",command=lambda:cleardata.accounts(1,masterpwd))
	delete.add_command(label="Twitter",command=lambda:cleardata.accounts(2,masterpwd))
	delete.add_command(label="Backpack",command=lambda:cleardata.accounts(3,masterpwd))
	delete.add_command(label="Instagram",command=lambda:cleardata.accounts(4,masterpwd))
	delete.add_command(label="Gmail",command=lambda:cleardata.accounts(5,masterpwd))
	delete.add_command(label="Drive",command=lambda:cleardata.accounts(7,masterpwd))
	delete.add_command(label="Youtube",command=lambda:cleardata.accounts(8,masterpwd))
	login.add_cascade(label="Delete",menu=delete)

	menubar.add_cascade(label="Credentials",menu=login)

	auto=Menu(menubar,tearoff=0)
	auto.add_command(label="Launch", command=lambda:autologin.launch(masterpwd))
	auto.add_command(label="Settings", command=lambda:autologin.settings(masterpwd))
	menubar.add_cascade(label="Autologin",menu=auto)

	mGUI.config(menu=menubar)

def seekloginauto(num,subGUI):
	
	"""
	Executes the seek login commands depending upon requirement. Instructed through num
	"""

	subGUI.destroy()

	if(num==1):
		credentials.seekfblogin(masterpwd)
	if(num==2):
		credentials.seektwitterlogin(masterpwd)
	if(num==3):
		credentials.seekbackpacklogin(masterpwd)
	if(num==4):
		credentials.seekinstalogin(masterpwd)
	if(num==5):
		credentials.seekgmaillogin(masterpwd)
	if(num==7):
		credentials.seekdrivelogin(masterpwd)
	if(num==8):
		credentials.seekyoutubelogin(masterpwd)	

def loginauto(num):

	"""
	Executes the login commands depending upon requirement. Instructed through num
	"""
	global masterpwd 

	if(num==1):
		login.facebook(masterpwd)
	elif(num==2):
		login.twitter(masterpwd)
	elif(num==3):
		login.backpack(masterpwd)
	elif(num==4):
		login.instagram(masterpwd)
	elif(num==5):
		login.gmail(masterpwd)
	elif(num==7):
		login.drive(masterpwd)
	elif(num==8):
		login.youtube(masterpwd)

def credentialcheck(num):

	"""
	Produces an alert if credentials are not preset by the user, but tries to access the web application
	"""

	global masterpwd
	i=1
	os.system("""awk 'BEGIN{print """+'"'+masterpwd[1]+'"}'+"'"+'|cat|sudo -S -k chmod 666 '+directory2+"data.txt")
	with open(directory+"data.txt","r") as file:
		for line in file:
			if(i==num):
				data=line
			i+=1	
	os.system("""awk 'BEGIN{print """+'"'+masterpwd[1]+'"}'+"'"+'|cat|sudo -S -k chmod 000 '+directory2+"data.txt")
	data=data.rstrip("\n")
	space=data.find(" ")
	user=data[:space]
	passwd=data[space+1:]
	if(user=="user" and passwd=="pass"):
		
		subGUI=Toplevel()
		subGUI.wm_iconbitmap(bitmap="@LoginAT_logo.xbm")
		border=Canvas(subGUI,width=400,height=200)
		border.pack()
		border.create_rectangle(6,6,394,194,width=0, fill="#e0ffff")
		subGUI.geometry("400x200")
		subGUI.resizable(width=False,height=False)
		subGUI.title("Error")
		errorlabel1=Label(subGUI,text="The credentials have not been set",bg="#e0ffff",font=(None,14)).place(x=32,y=40)
		errorlabel2=Label(subGUI,text="Click here to set",bg="#e0ffff",font=(None,14)).place(x=120,y=80)
		setbutton=Button(subGUI,text="Set",padx=5,pady=5,font=(None,14,"bold"),command=lambda:seekloginauto(num,subGUI)).place(x=172,y=130)		
	else:
		loginauto(num)


def GUIwindow():

	"""
	This function defines the initial GUI screen
	"""

	# GUI Initialization	

	mGUI=Tk()
	mGUI.wm_iconbitmap(bitmap="@LoginAT_logo.xbm")
	mGUI.resizable(width=False,height=False)	
	border=Canvas(mGUI, width=700, height=426)
	border.pack()
	border.create_rectangle(6,6,694,80,width=0, fill="#e0ffff")
	border.create_rectangle(6,86,694,420,width=0, fill="#e0ffff")	
	mGUI.geometry('700x426')
	mGUI.title("LoginAT")
	head=Label(mGUI,text="LoginAT",font=(None,25,"bold"),bg="#e0ffff").place(x=265,y=20)

	# Facebook button

	fbimage=PhotoImage(file=directory+"facebook.png")
	fbimage=fbimage.subsample(5,5)
	facebook=Label(mGUI,image=fbimage).place(x=20,y=100)
	fbbutton=Button(mGUI,text="Facebook",font=(None,25),pady=11,padx=21,command=lambda:credentialcheck(1)).place(x=90,y=100)

	# Twitter button

	twitterimage=PhotoImage(file=directory+"twitter.png")
	twitterimage=twitterimage.subsample(5,5)
	twitter=Label(mGUI,image=twitterimage).place(x=375,y=100)
	twitterbutton=Button(mGUI,text="Twitter",font=(None,25),pady=11,padx=48,command=lambda:credentialcheck(2)).place(x=445,y=100)

	# backpack button

	backpackimage=PhotoImage(file=directory+"backpack.png")
	backpackimage=backpackimage.subsample(5,5)
	backpack=Label(mGUI,image=backpackimage).place(x=20,y=180)
	backpackbutton=Button(mGUI,text="Backpack",font=(None,25),pady=11,padx=21,command=lambda:credentialcheck(3)).place(x=90,y=180)

	# Instagram button

	instaimage=PhotoImage(file=directory+"insta.png")
	instaimage=instaimage.subsample(5,5)
	insta=Label(mGUI,image=instaimage).place(x=375,y=180)
	instabutton=Button(mGUI,text="Instagram",font=(None,25),pady=11,padx=22,command=lambda:credentialcheck(4)).place(x=445,y=180)

	# Gmail button

	gmailimage=PhotoImage(file=directory+"gmail.png")
	gmailimage=gmailimage.subsample(5,5)
	gmail=Label(mGUI,image=gmailimage).place(x=20,y=260)
	gmailbutton=Button(mGUI,text="Gmail",font=(None,25),pady=11,padx=52,command=lambda:credentialcheck(5)).place(x=90,y=260)

	# Whatsapp button

	whatsappimage=PhotoImage(file=directory+"whatsapp.png")
	whatsappimage=whatsappimage.subsample(5,5)
	whatsapp=Label(mGUI,image=whatsappimage).place(x=375,y=260)
	whatsappbutton=Button(mGUI,text="Whatsapp",font=(None,25),pady=11,padx=23,command=lambda:login.whatsapp()).place(x=445,y=260)

	# Google Drive button

	driveimage=PhotoImage(file=directory+"drive.png")
	driveimage=driveimage.subsample(5,5)
	drive=Label(mGUI,image=driveimage).place(x=20,y=340)
	drivebutton=Button(mGUI,text="Drive",font=(None,25),pady=11,padx=56,command=lambda:credentialcheck(7)).place(x=90,y=340)

	# Youtube button

	youtubeimage=PhotoImage(file=directory+"youtube.png")
	youtubeimage=youtubeimage.subsample(5,5)
	youtube=Label(mGUI,image=youtubeimage).place(x=375,y=340)
	youtubebutton=Button(mGUI,text="Youtube",font=(None,25),pady=11,padx=39,command=lambda:credentialcheck(8)).place(x=445,y=340)

	# Adding menu buttons

	menubutton(mGUI)

	mGUI.mainloop()	

if(__name__=="__main__"):
	boot()

