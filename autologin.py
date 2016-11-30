# autologin.py
# Author: Nihesh Anderson K
# Nov 1, 2016

"""
This module enables the single click login feature for all enabled apps
"""

from tkinter import *
from login import loginretrieve
import login
import os
import pyautogui

directory=""
directory2=""

user=None
passwd=None
flag=1

def usercount(num,masterpwd):
	
	"""
	Returns number of users in the given category
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

	return count

def settings(masterpwd):
	
	"""
	Prompts the user to select apps to work using autologin
	"""

	count1=usercount(1,masterpwd)
	count2=usercount(2,masterpwd)
	count3=usercount(3,masterpwd)
	count4=usercount(4,masterpwd)
	count5=usercount(5,masterpwd)
	count7=usercount(7,masterpwd)
	count8=usercount(8,masterpwd)

	settings=[[],[],[],[],[],[],[],[]]
	list=[[],[],[],[],[],[],[],[]]

	row1=max(count1,count2,count3,count4)
	row2=max(count5,count7,count8)

	textspace=35

	file=open(directory+"settings.txt","r")
	i=0
	for line in file:
		line=line.rstrip("\n")
		if(line!=""):
			line=int(line)
			while line>0:
				settings[i].append(line%10)
				line=line//10
		i+=1
	file.close()

	subGUI=Toplevel()
	subGUI.wm_iconbitmap(bitmap="@LoginAT_logo.xbm")
	string=str(335+(textspace*(row2+row1)))
	subGUI.geometry('1400x'+string)
	subGUI.title("Settings")
	subGUI.resizable(width=False,height=False)	
	border=Canvas(subGUI, width=1400, height=334+(textspace*(row1+row2)))
	border.pack()
	border.create_rectangle(6,6,1394,80,width=0, fill="#e0ffff")
	border.create_rectangle(6,86,1394,330+(textspace*(row1+row2)),width=0, fill="#e0ffff")	

	head=Label(subGUI,text="Choose the apps to be launched",font=(None,20),bg="#e0ffff").place(x=470,y=28)

	head1=Label(subGUI,text="Facebook",font=(None,20,"bold"),bg="#e0ffff").place(x=120,y=110)
	fbvar=[None]*count1
	check1=[None]*count1
	for i in range(count1):
		fbvar[i]=IntVar()

	if(loginretrieve(1,i+1,masterpwd,subGUI,1)=="Data not set"):
		label1=Label(subGUI,text="Data not set",fg="#FF0000",font=(None,18),bg="#e0ffff").place(x=118,y=155+(textspace*i))
	else:
		for i in range(count1):
			check1[i]=Checkbutton(subGUI,font=(None,12),anchor=W,width=25,borderwidth=0,text=loginretrieve(1,i+1,masterpwd,subGUI,1),variable=fbvar[i]).place(x=50,y=155+(textspace*i))
			list[0].append(fbvar[i])
			if (i+1) in settings[0]:
				fbvar[i].set(1)

	head2=Label(subGUI,text="Twitter",font=(None,20,"bold"),bg="#e0ffff").place(x=470,y=110)
	twittervar=[None]*count2
	check2=[None]*count2
	for i in range(count2):
		twittervar[i]=IntVar()

	if(loginretrieve(2,i+1,masterpwd,subGUI,1)=="Data not set"):
		label2=Label(subGUI,text="Data not set",fg="#FF0000",font=(None,18),bg="#e0ffff").place(x=448,y=155+(textspace*i))
	else:
		for i in range(count2):
			check2[i]=Checkbutton(subGUI,font=(None,12),anchor=W,width=25,borderwidth=0,text=loginretrieve(2,i+1,masterpwd,subGUI,1),variable=twittervar[i]).place(x=385,y=155+(textspace*i))
			list[1].append(twittervar[i])
			if (i+1) in settings[1]:
				twittervar[i].set(1)

	head3=Label(subGUI,text="Backpack",font=(None,20,"bold"),bg="#e0ffff").place(x=780,y=110)

	bpvar=[None]*count3
	check3=[None]*count3
	for i in range(count3):
		bpvar[i]=IntVar()

	if(loginretrieve(3,i+1,masterpwd,subGUI,1)=="Data not set"):
		label3=Label(subGUI,text="Data not set",fg="#FF0000",font=(None,18),bg="#e0ffff").place(x=777,y=155+(textspace*i))
	else:
		for i in range(count3):
			check3[i]=Checkbutton(subGUI,font=(None,12),anchor=W,width=25,borderwidth=0,text=loginretrieve(3,i+1,masterpwd,subGUI,1),variable=bpvar[i]).place(x=720,y=155+(textspace*i))
			list[2].append(bpvar[i])
			if (i+1) in settings[2]:
				bpvar[i].set(1)

	head4=Label(subGUI,text="Instagram",font=(None,20,"bold"),bg="#e0ffff").place(x=1120,y=110)
	instavar=[None]*count4
	check4=[None]*count4
	for i in range(count4):
		instavar[i]=IntVar()

	if(loginretrieve(4,i+1,masterpwd,subGUI,1)=="Data not set"):
		label4=Label(subGUI,text="Data not set",fg="#FF0000",font=(None,18),bg="#e0ffff").place(x=1120,y=155+(textspace*i))
	else:
		for i in range(count4):
			check4[i]=Checkbutton(subGUI,font=(None,12),anchor=W,width=25,borderwidth=0,text=loginretrieve(4,i+1,masterpwd,subGUI,1),variable=instavar[i]).place(x=1060,y=155+(textspace*i))
			list[3].append(instavar[i])
			if (i+1) in settings[3]:
				instavar[i].set(1)

	head5=Label(subGUI,text="Gmail",font=(None,20,"bold"),bg="#e0ffff").place(x=320,y=190+(textspace*row1))
	gmailvar=[None]*count5
	check5=[None]*count5
	for i in range(count5):
		gmailvar[i]=IntVar()

	if(loginretrieve(5,i+1,masterpwd,subGUI,1)=="Data not set"):
		label5=Label(subGUI,text="Data not set",fg="#FF0000",font=(None,18),bg="#e0ffff").place(x=290,y=235+(textspace*(row1+i)))
	else:
		for i in range(count5):
			check5[i]=Checkbutton(subGUI,font=(None,12),anchor=W,width=25,borderwidth=0,text=loginretrieve(5,i+1,masterpwd,subGUI,1),variable=gmailvar[i]).place(x=230,y=235+(textspace*(row1+i)))
			list[4].append(gmailvar[i])
			if (i+1) in settings[4]:
				gmailvar[i].set(1)

	head7=Label(subGUI,text="Drive",font=(None,20,"bold"),bg="#e0ffff").place(x=655,y=190+(textspace*row1))
	drivevar=[None]*count7
	check7=[None]*count7
	for i in range(count7):
		drivevar[i]=IntVar()

	if(loginretrieve(7,i+1,masterpwd,subGUI,1)=="Data not set"):
		label7=Label(subGUI,text="Data not set",fg="#FF0000",font=(None,18),bg="#e0ffff").place(x=620,y=235+(textspace*(row1+i)))
	else:
		for i in range(count7):
			check7[i]=Checkbutton(subGUI,font=(None,12),anchor=W,width=25,borderwidth=0,text=loginretrieve(7,i+1,masterpwd,subGUI,1),variable=drivevar[i]).place(x=560,y=235+(textspace*(row1+i)))
			list[6].append(drivevar[i])
			if (i+1) in settings[6]:
				drivevar[i].set(1)

	head8=Label(subGUI,text="Youtube",font=(None,20,"bold"),bg="#e0ffff").place(x=960,y=190+(textspace*row1))
	youtubevar=[None]*count8
	check8=[None]*count8
	for i in range(count8):
		youtubevar[i]=IntVar()

	if(loginretrieve(8,i+1,masterpwd,subGUI,1)=="Data not set"):
		label8=Label(subGUI,text="Data not set",fg="#FF0000",font=(None,18),bg="#e0ffff").place(x=950,y=235+(textspace*(row1+i)))
	else:
		for i in range(count8):
			check8[i]=Checkbutton(subGUI,font=(None,12),anchor=W,width=25,borderwidth=0,text=loginretrieve(8,i+1,masterpwd,subGUI,1),variable=youtubevar[i]).place(x=890,y=235+(textspace*(row1+i)))
			list[7].append(youtubevar[i])
			if (i+1) in settings[7]:
				youtubevar[i].set(1)

	savebutton=Button(subGUI,text="OK",padx=20,pady=10,font=(None,18),command=lambda:savedata(subGUI,list)).place(x=657,y=260+(textspace*(row1+row2)))

def savedata(subGUI,list):

	""" 
	Stores changes made to settings
	"""
	for i in range(len(list)):
		for j in range(len(list[i])):
			list[i][j]=list[i][j].get()

	file=open(directory+"settings.txt","w")
	for i in range(len(list)):
		string=""
		for j in range(len(list[i])):	
			if(list[i][j]==1):
				string+=str(j+1)
		file.write(string+"\n")
	file.close()
	subGUI.destroy()



def launch(masterpwd):

	"""
	Launches all the preferred apps
	"""
	global flag,user,passwd
	settings=[[],[],[],[],[],[],[],[]]
	file=open(directory+"settings.txt","r")
	i=0
	for line in file:
		line=line.rstrip("\n")
		if(line!=""):
			line=int(line)
			while line>0:
				settings[i].append(line%10)
				line=line//10
		i+=1
	file.close()

	for i in range(len(settings)):
		for j in range(len(settings[i])):
			login.loginretrieve(i+1,settings[i][j],masterpwd,mode=2)

if __name__=="__main__":
	
	pass
	# Test the module here
