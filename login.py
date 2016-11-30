# login.py
# Author: Nihesh Anderson K
# 30 Sept 2016

import time
from tkinter import *
import selenium
from selenium import webdriver
import http
import base64
import string
from hashlib import md5
from Crypto.Cipher import AES
import string
import base64
import os
import pyautogui

directory=""
directory2=""
driverpath=os.path.abspath("")
slash=driverpath.find("/",1)
slash=driverpath.find("/",slash+1)
driverpath=driverpath[:slash+1]
driverpath=driverpath+"Desktop/geckodriver"

"""
This module uses selenium webdriver to log into different websites
"""

user=None
passwd=None
flag=0

def pad(text):

	""" 
	Pads with { to convert the string into 32 characters
	"""

	return text+("{"*(32-len(text)))

def showpass(masterpwd,num,i,mGUI,a1,a2,a3):

	"""
	Decrypts and presents the password to the user
	"""

	ans1=a1.get()
	ans2=a2.get()
	ans3=a3.get()
	os.system("""awk 'BEGIN{print """+'"'+masterpwd[1]+'"}'+"'"+'|cat|sudo -S -k chmod 666 '+directory2+"questions.txt")
	file=open("questions.txt","r")
	t=1
	for line in file:
		line=line.rstrip("\n")
		if(t==2):
			a1hash=line
		if(t==4):
			a2hash=line
		if(t==6):
			a3hash=line
		t+=1
	file.close()
	os.system("""awk 'BEGIN{print """+'"'+masterpwd[1]+'"}'+"'"+'|cat|sudo -S -k chmod 000 '+directory2+"questions.txt")
	if(a1hash==md5(ans1.encode()).hexdigest() and a2hash==md5(ans2.encode()).hexdigest() and a3hash==md5(ans3.encode()).hexdigest()):
		mGUI.destroy()
		mGUI=Toplevel()
		mGUI.wm_iconbitmap(bitmap="@LoginAT_logo.xbm")
		mGUI.title("Password")
		border=Canvas(mGUI,width=400,height=150)
		border.pack()
		border.create_rectangle(6,6,394,50,width=0, fill="#e0ffff")
		border.create_rectangle(6,56,394,144,width=0, fill="#e0ffff")	
		mGUI.geometry("400x150")		
		mGUI.resizable(width=False,height=False)
		label=Label(mGUI,text="Password",font=(None,14,"bold"),bg="#e0ffff").place(x=140,y=15)
		passwd=loginretrieve(num,i,masterpwd,subGUI=None,mode=2)
		label2=Label(mGUI,text=passwd,font=(None,14,),bg="#e0ffff").place(x=120,y=85)
	
	else:
		return


def showpassauth(num,i,masterpwd):

	"""
	Authenticates entry into decryption module
	"""

	mGUI=Toplevel()
	mGUI.wm_iconbitmap(bitmap="@LoginAT_logo.xbm")
	mGUI.title("Password")
	border=Canvas(mGUI,width=400,height=370)
	border.pack()
	border.create_rectangle(6,6,394,50,width=0, fill="#e0ffff")
	border.create_rectangle(6,56,394,364,width=0, fill="#e0ffff")	
	mGUI.geometry("400x370")		
	mGUI.resizable(width=False,height=False)
	a1=StringVar()
	a2=StringVar()
	a3=StringVar()
	os.system("""awk 'BEGIN{print """+'"'+masterpwd[1]+'"}'+"'"+'|cat|sudo -S -k chmod 666 '+directory2+"questions.txt")
	file=open("questions.txt","r")
	t=1
	for line in file:
		line=line.rstrip("\n")
		if(t==1):
			q1=line
		if(t==3):
			q2=line
		if(t==5):
			q3=line
		t+=1
	file.close()
	os.system("""awk 'BEGIN{print """+'"'+masterpwd[1]+'"}'+"'"+'|cat|sudo -S -k chmod 000 '+directory2+"questions.txt")
	label=Label(mGUI,text="AUTHENTICATION",font=(None,12,"bold"),bg="#e0ffff").place(x=120,y=20)
	sublabel3=Label(mGUI,text="Question 1",font=(None,12),bg="#e0ffff").place(x=20,y=80)
	sublabel4=Label(mGUI,text="Answer",font=(None,12),bg="#e0ffff").place(x=20,y=120)
	sublabel5=Label(mGUI,text="Question 2",font=(None,12),bg="#e0ffff").place(x=20,y=160)
	sublabel6=Label(mGUI,text="Answer",font=(None,12),bg="#e0ffff").place(x=20,y=200)
	sublabel7=Label(mGUI,text="Question 3",font=(None,12),bg="#e0ffff").place(x=20,y=240)
	sublabel8=Label(mGUI,text="Answer",font=(None,12),bg="#e0ffff").place(x=20,y=280)
	qlabel1=Label(mGUI,text=q1,font=(None,12),bg="#e0ffff").place(x=200,y=80)	
	entry4=Entry(mGUI,textvariable=a1,font=(None,11),width=17,show="*")
	entry4.place(x=200,y=120)	
	qlabel2=Label(mGUI,text=q2,font=(None,12),bg="#e0ffff").place(x=200,y=160)
	entry6=Entry(mGUI,textvariable=a2,font=(None,11),width=17,show="*")
	entry6.place(x=200,y=200)	
	qlabel3=Label(mGUI,text=q3,font=(None,12),bg="#e0ffff").place(x=200,y=240)
	entry8=Entry(mGUI,textvariable=a3,font=(None,11),width=17,show="*")
	entry8.place(x=200,y=280)	
	decrypt=Button(mGUI,text="Decrypt",font=(None,12),command=lambda:showpass(masterpwd,num,i,mGUI,a1,a2,a3)).place(x=160,y=320)
	

def loginretrieve(num,i,masterpwd,subGUI=None,mode=0):

	"""
	Decodes the password and stores it in the global variable user and passwd
	"""
		
	global user,passwd,flag

	j=1
	os.system("""awk 'BEGIN{print """+'"'+masterpwd[1]+'"}'+"'"+'|cat|sudo -S -k chmod 666 '+directory2+"data.txt")
	file=open(directory+"data.txt","r")
	for line in file:
		if(j==num):
			data=line
			count=(line.count(" ")+1)//2
		j+=1
	file.close()
	os.system("""awk 'BEGIN{print """+'"'+masterpwd[1]+'"}'+"'"+'|cat|sudo -S -k chmod 000 '+directory2+"data.txt")
	data=data.rstrip("\n")
	if(data=="user pass"):
		return "Data not set"
	if(count>1):	
		start=0
		end=data.find(" ")
		end=data.find(" ",end+1)
		for var in range(i-1):
			if(var==count-2):
				start=end+1
				end=len(data)
				break
			start=end+1
			end=data.find(" ",start)
			end=data.find(" ",end+1)
		data=data[start:end]
	space=data.find(" ")
	user=data[:space]
	passwd=data[space+1:]
	aes=AES.new(pad(masterpwd[0]))
	user=aes.decrypt(base64.b64decode(user.encode()))
	user=user.decode("utf-8")
	user=user.rstrip("{")
	passwd=aes.decrypt(base64.b64decode(passwd.encode()))
	passwd=passwd.decode("utf-8")
	passwd=passwd.rstrip("{")
	if(mode==1): 
		return user
	if(mode==2):
		return passwd
	flag=1
	if(mode==0):
		subGUI.destroy()
	if(num==1):
		facebook(masterpwd)
	elif(num==2):
		twitter(masterpwd)
	elif(num==3):
		backpack(masterpwd)
	elif(num==4):
		instagram(masterpwd)
	elif(num==5):
		gmail(masterpwd)
	elif(num==7):
		drive(masterpwd)
	elif(num==8):
		youtube(masterpwd)

	
def seekcredentials(num,masterpwd): 

	"""
	This function is used let the user to choose which account to log into
	"""

	i=1

	os.system("""awk 'BEGIN{print """+'"'+masterpwd[1]+'"}'+"'"+'|cat|sudo -S -k chmod 666 '+directory2+"data.txt")
	file=open(directory+"data.txt","r")
	for line in file:
		if(i==num):
			data=line
			count=(line.count(" ")+1)//2
		i+=1
	file.close()
	os.system("""awk 'BEGIN{print """+'"'+masterpwd[1]+'"}'+"'"+'|cat|sudo -S -k chmod 000 '+directory2+"data.txt")

	data=data.rstrip("\n")	

	if(num==1):
		titlebox="Facebook"
	elif(num==2):
		titlebox="twitter"
	elif(num==3):
		titlebox="Backpack"
	elif(num==4):
		titlebox="Instagram"	
	elif(num==5):
		titlebox="Gmail"
	elif(num==7):
		titlebox="Google Drive"			
	elif(num==8):
		titlebox="Youtube"	

	subGUI=Toplevel()
	subGUI.wm_iconbitmap(bitmap="@LoginAT_logo.xbm")

	subGUI.title(titlebox)
	subGUI.geometry("560x"+str((60*count)+40))
	border=Canvas(subGUI,width=560,height=(60*count)+40)
	border.pack()
	border.create_rectangle(6,6,554,(60*count)+34,width=0, fill="#7FFFD4")
	subGUI.resizable(width=False,height=False)
	label1=[None]*count
	buttondel=[None]*count
	passwd=[None]*count
	aes=AES.new(pad(masterpwd[0]))

	start=0
	end=data.find(" ")	
	for i in range(count):
		user=data[start:end]		
		user=aes.decrypt(base64.b64decode(user.encode()))
		user=user.decode("utf-8")
		user=user.rstrip("{")
		border.create_rectangle(6,31+(60*i),554,77+(60*i),width=0, fill="#E0FFFF")
		label1[i]=Label(subGUI,text=user,font=(None,13),bg="#E0FFFF").place(x=30,y=42+(60*i))
		buttondel[i]=Button(subGUI,text="Login",command=lambda i=i:loginretrieve(num,i+1,masterpwd,subGUI),font=(None,13),padx=5,pady=5).place(x=390,y=35+(60*i))
		passwd[i]=Button(subGUI,text="Pass",command=lambda i=i:showpassauth(num,i+1,masterpwd),font=(None,13),padx=8,pady=5).place(x=470,y=35+(60*i))
		if(i!=count-1):
			start=(data.find(" ",end+1))+1
			end=data.find(" ",start+1)

def facebook(masterpwd):
	
	"""
	Logs into facebook using given user input
	"""
	global user,passwd,flag,driverpath
	
	try: 
		if(flag==0):
			seekcredentials(1,masterpwd)
			return
		flag=0
		driver=webdriver.Firefox(executable_path=driverpath)
		driver.maximize_window()
		driver.get("https://www.facebook.com/")
		userfield=driver.find_element_by_id("email")
		userfield.clear()
		userfield.send_keys(user)
		passfield=driver.find_element_by_id("pass")	
		passfield.clear()
		passfield.send_keys(passwd)	
		driver.find_element_by_id("u_0_l").click()
		
	except (selenium.common.exceptions.ElementNotVisibleException,selenium.common.exceptions.NoSuchElementException,http.client.RemoteDisconnected,selenium.common.exceptions.WebDriverException):
	
		pass		
		
def twitter(masterpwd):
	
	"""
	Logs into twitter using given user input
	"""
	
	global user,passwd,flag,driverpath

	try:

		if(flag==0):
			seekcredentials(2,masterpwd)
			return
		flag=0
		driver=webdriver.Firefox(executable_path=driverpath)
		driver.maximize_window()
		driver.get("https://twitter.com/")
		driver.find_element_by_css_selector("a[href*='/login']").click()
		userfield=driver.find_element_by_name("session[username_or_email]")
		userfield.clear()
		userfield.send_keys(user)
		passfield=driver.find_element_by_name("session[password]")	
		passfield.clear()
		passfield.send_keys(passwd)	
		driver.find_element_by_css_selector("input[value*='Log in']").click()
		
	except (selenium.common.exceptions.WebDriverException,selenium.common.exceptions.ElementNotVisibleException,selenium.common.exceptions.NoSuchElementException,http.client.RemoteDisconnected):
		
		pass

def backpack(masterpwd):
	
	"""
	Logs into backpack using given user input
	"""

	global user,passwd,flag,driverpath

	try:

		if(flag==0):
			seekcredentials(3,masterpwd)
			return
		flag=0
	
		driver=webdriver.Firefox(executable_path=driverpath)
		driver.maximize_window()
		driver.get("https://www.usebackpack.com/")
		driver.find_element_by_id("loginButton").click()	
		userfield=driver.find_element_by_id("user_email")
		userfield.clear()
		userfield.send_keys(user)
		passfield=driver.find_element_by_id("user_password")	
		passfield.clear()
		passfield.send_keys(passwd)	
		driver.find_element_by_css_selector("input[value*='Sign in']").click()
		
	except (selenium.common.exceptions.WebDriverException,selenium.common.exceptions.ElementNotVisibleException,selenium.common.exceptions.NoSuchElementException,http.client.RemoteDisconnected):
		
		pass

def instagram(masterpwd):
	
	"""
	Logs into instagram using given user input
	"""

	global user,passwd,flag,driverpath

	try:
	
		if(flag==0):
			seekcredentials(4,masterpwd)
			return
		flag=0 
	
		driver=webdriver.Firefox(executable_path=driverpath)
		driver.maximize_window()
		driver.get("https://www.instagram.com/")
	
		while True:
		
			try:	
				driver.find_element_by_css_selector("a[href*='javascript:;']").click()
				userfield=driver.find_element_by_name("username")
				userfield.clear()
				userfield.send_keys(user)
				passfield=driver.find_element_by_name("password")	
				passfield.clear()
				passfield.send_keys(passwd)	
				driver.find_element_by_css_selector("button[class*='_aj7mu _taytv _ki5uo _o0442']").click()
				break
	
			except selenium.common.exceptions.NoSuchElementException:
				pass
	
	except (selenium.common.exceptions.WebDriverException,selenium.common.exceptions.ElementNotVisibleException,selenium.common.exceptions.NoSuchElementException,http.client.RemoteDisconnected):
		
		pass
		
def gmail(masterpwd):
	
	"""
	Logs into gmail using given user input
	"""

	global user,passwd,flag,driverpath

	try:
		
		if(flag==0):
			seekcredentials(5,masterpwd)
			return
		flag=0
	
		driver=webdriver.Firefox(executable_path=driverpath)
		driver.maximize_window()
		driver.get("https://mail.google.com/")
		while True:
			try:	
				userfield=driver.find_element_by_id("Email")
				userfield.clear()
				userfield.send_keys(user)
				driver.find_element_by_id("next").click()
				while True:			
					try:		
						passfield=driver.find_element_by_css_selector("input[id*='Passwd']")	
						passfield.clear()
						passfield.send_keys(passwd)	
						driver.find_element_by_id("signIn").click()
						break
					except (selenium.common.exceptions.InvalidElementStateException,selenium.common.exceptions.StaleElementReferenceException,http.client.RemoteDisconnected):
						pass
				break
			except selenium.common.exceptions.NoSuchElementException:
				pass

	except (selenium.common.exceptions.WebDriverException,selenium.common.exceptions.ElementNotVisibleException,selenium.common.exceptions.NoSuchElementException,http.client.RemoteDisconnected):
	
		pass

def whatsapp():
	
	"""
	Logs into whatsapp using given user input
	"""

	global driverpath

	try:
		
		driver=webdriver.Firefox(executable_path=driverpath)
		driver.maximize_window()
		driver.get("https://web.whatsapp.com/")
		
	except (selenium.common.exceptions.WebDriverException,selenium.common.exceptions.ElementNotVisibleException,selenium.common.exceptions.NoSuchElementException,http.client.RemoteDisconnected):
		
		pass

def drive(masterpwd):
	
	"""
	Logs into drive using given user input
	"""

	global user,passwd,flag,driverpath

	try:
		
		if(flag==0):
			seekcredentials(7,masterpwd)
			return
		flag=0

		driver=webdriver.Firefox(executable_path=driverpath)
		driver.maximize_window()
		driver.get("https://www.google.com/drive")
		driver.find_element_by_link_text("Go to Google Drive").click()
		while True:
			try:	
				userfield=driver.find_element_by_id("Email")
				userfield.clear()
				userfield.send_keys(user)
				driver.find_element_by_id("next").click()
				while True:			
					try:		
						passfield=driver.find_element_by_css_selector("input[id*='Passwd']")	
						passfield.clear()
						passfield.send_keys(passwd)	
						driver.find_element_by_id("signIn").click()
						
						break
					except (selenium.common.exceptions.InvalidElementStateException,selenium.common.exceptions.StaleElementReferenceException,http.client.RemoteDisconnected):
						pass
				break
			except selenium.common.exceptions.NoSuchElementException:
				pass

	except (selenium.common.exceptions.WebDriverException,selenium.common.exceptions.ElementNotVisibleException,selenium.common.exceptions.NoSuchElementException,http.client.RemoteDisconnected):
	
		pass

def youtube(masterpwd): 
	
	"""
	Logs into youtube using given user input
	"""

	global user,passwd,flag,driverpath	

	try:	

		if(flag==0):
			seekcredentials(8,masterpwd)
			return
		flag=0
		
		driver=webdriver.Firefox(executable_path=driverpath)
		driver.maximize_window()
		driver.get("https://www.youtube.com/")
		driver.find_element_by_css_selector("button[class*='yt-uix-button yt-uix-button-size-default yt-uix-button-primary']").click()
		while True:
			try:	
				userfield=driver.find_element_by_id("Email")
				userfield.clear()
				userfield.send_keys(user)
				driver.find_element_by_id("next").click()
				while True:			
					try:		
						passfield=driver.find_element_by_css_selector("input[id*='Passwd']")	
						passfield.clear()
						passfield.send_keys(passwd)	
						driver.find_element_by_id("signIn").click()
						
						break
					except (selenium.common.exceptions.InvalidElementStateException,selenium.common.exceptions.StaleElementReferenceException,http.client.RemoteDisconnected):
						pass
				break
			except selenium.common.exceptions.NoSuchElementException:
				pass

	except (selenium.common.exceptions.WebDriverException,selenium.common.exceptions.ElementNotVisibleException,selenium.common.exceptions.NoSuchElementException,http.client.RemoteDisconnected):
	
		pass

if(__name__=="__main__"):
	pass

	# test the module here 

