# initaccess.py
# Author: Nihesh Anderson K
# 4 Oct 2016

from Crypto.Cipher import AES
import string
from tkinter import *
import sys
from hashlib import md5
import os
from login import pad
import base64
import homeGUI
import random

directory=""
directory2=""

"""
This module is used to grant access for the user to enter into the application. It also takes care of secure
encryption and decryption of data
"""

def rootvalidate(root):

	"""
	Checks if the given root password is valid or not
	"""

	filename=random.randint(0,10000)
	filename=str(filename)
	tempfile=open(directory+filename,"w")
	tempfile.write("testing")
	tempfile.close()
	try:	
		os.system("""awk 'BEGIN{print """+'"'+root+'"}'+"'"+'|cat|sudo -S -k chattr +i '+directory2+filename)
		tempfile=open(directory+filename,"w")
		tempfile.write("testing")
		tempfile.close()
		os.remove(directory+filename)		
		return False		
	except:
		os.system("""awk 'BEGIN{print """+'"'+root+'"}'+"'"+'|cat|sudo -S -k chattr -i '+directory2+filename)
		os.remove(directory+filename)
		return True


def storedata(root,passwd,mGUI,q1,a1,q2,a2,q3,a3):
	
	"""
	Stores master password and locks it
	"""
	q1=q1.get()
	q2=q2.get()
	q3=q3.get()
	a1=a1.get()
	a2=a2.get()
	a3=a3.get()
	root=root.get()
	passwd=passwd.get()
	if(not rootvalidate(root)):
		label=Label(mGUI,text="X",font=(None,12),bg="#e0ffff",fg="#FF0000").place(x=180,y=110)
		return
	file=open(directory+"master.txt","w")
	file.write(md5(passwd.encode()).hexdigest())	
	file.close()
	os.system("""awk 'BEGIN{print """+'"'+root+'"}'+"'"+'|cat|sudo -S -k chattr +i '+directory2+'master.txt')
	file=open("questions.txt","w")
	file.write(q1+"\n")
	file.write(md5(a1.encode()).hexdigest()+"\n")
	file.write(q2+"\n")
	file.write(md5(a2.encode()).hexdigest()+"\n")
	file.write(q3+"\n")
	file.write(md5(a3.encode()).hexdigest()+"\n")
	file.close()
	os.system("""awk 'BEGIN{print """+'"'+root+'"}'+"'"+'|cat|sudo -S -k chmod 000 '+directory2+"questions.txt")
	file=open("data.txt","w")
	file.write("user pass\nuser pass\nuser pass\nuser pass\nuser pass\nuser pass\nuser pass\nuser pass\n")
	file.close()
	os.system("""awk 'BEGIN{print """+'"'+root+'"}'+"'"+'|cat|sudo -S -k chown root:root '+directory2+'data.txt')
	os.system("""awk 'BEGIN{print """+'"'+root+'"}'+"'"+'|cat|sudo -S -k chmod 000 '+directory2+'data.txt')
	file=open("settings.txt","w")
	file.write("\n\n\n\n\n\n\n\n")
	file.close()
	mGUI.destroy()	

def changedata(root,old,new,mGUI,entry1,entry2,entry3,mainGUI):
	
	"""
	Unlocks master file, modifies master password and locks it
	"""

	root=root.get()
	old=old.get()
	new=new.get()
	file=open(directory+"master.txt","r")
	for line in file:
		if(line==md5(old.encode()).hexdigest() and rootvalidate(root) and md5(new.encode()).hexdigest()!="d41d8cd98f00b204e9800998ecf8427e"):
			os.system("""awk 'BEGIN{print """+'"'+root+'"}'+"'"+"|cat|sudo -S -k chattr -i "+directory2+"master.txt")
			os.remove(directory+"master.txt")
			file=open(directory+"master.txt","w")
			file.write(md5(new.encode()).hexdigest())	
			file.close()
			os.system("""awk 'BEGIN{print """+'"'+root+'"}'+"'"+"|cat|sudo -S -k chattr +i "+directory2+"master.txt")
			aesold=AES.new(pad(old).encode())
			aesnew=AES.new(pad(new).encode())
			newfile=open(directory+"temp.txt","w")
			os.system("""awk 'BEGIN{print """+'"'+root+'"}'+"'"+'|cat|sudo -S -k chmod 666 '+directory2+"data.txt")
			with open(directory+"data.txt","r") as file:
				for line in file:
					text=""
					l=[]
					line=line.rstrip("\n")
					user=line[:line.find(" ")]
					passwd=line[(line.find(" "))+1:]
					if(user!="user" and passwd!="pass" and user!="" and passwd!=""):
						details=line.split(" ")
						for val in range(len(details)):					
							l.append(details[val])						
							l[val]=base64.b64decode(l[val].encode())
							l[val]=aesold.decrypt(l[val])
							l[val]=aesnew.encrypt(l[val])
							l[val]=base64.b64encode(l[val])
							l[val]=l[val].decode()
							text+=l[val]+" "
						line=text[:len(text)-1]
					newfile.write(line+"\n")
			os.remove(directory+"data.txt")
			os.rename(directory+"temp.txt",directory+"data.txt")
			newfile.close()
			os.system("""awk 'BEGIN{print """+'"'+root+'"}'+"'"+'|cat|sudo -S -k chown root:root '+directory2+"data.txt")
			os.system("""awk 'BEGIN{print """+'"'+root+'"}'+"'"+'|cat|sudo -S -k chmod 000 '+directory2+"data.txt")
			mGUI.destroy()
			mainGUI.destroy()
			homeGUI.boot()	
		else:
			entry1.delete(0,END)
			entry2.delete(0,END)
			entry3.delete(0,END)	
	file.close()
			
def initmaster():

	"""
	Sets the master password for the first time
	"""

	mGUI=Tk()
	mGUI.wm_iconbitmap(bitmap="@LoginAT_logo.xbm")
	mGUI.title("Password Manager")
	border=Canvas(mGUI,width=400,height=440)
	border.pack()
	border.create_rectangle(6,6,394,50,width=0, fill="#e0ffff")
	border.create_rectangle(6,56,394,434,width=0, fill="#e0ffff")	
	mGUI.geometry("400x440")		
	mGUI.resizable(width=False,height=False)
	root=StringVar()
	passwd=StringVar()
	q1=StringVar()
	q2=StringVar()
	q3=StringVar()
	a1=StringVar()
	a2=StringVar()
	a3=StringVar()
	toplabel=Label(mGUI,text="Set Master Password",font=(None,14,"bold"),bg="#e0ffff").place(x=80,y=15)	
	sublabel1=Label(mGUI,text="Master Password",font=(None,12),bg="#e0ffff").place(x=20,y=70)
	entry1=Entry(mGUI,textvariable=passwd,font=(None,11),width=17,show="*").place(x=200,y=70)	
	entry2=Entry(mGUI,textvariable=root,font=(None,11),width=17,show="*").place(x=200,y=110)	
	sublabel2=Label(mGUI,text="Root Password",font=(None,12),bg="#e0ffff").place(x=20,y=110)
	sublabel3=Label(mGUI,text="Question 1",font=(None,12),bg="#e0ffff").place(x=20,y=150)
	sublabel4=Label(mGUI,text="Answer",font=(None,12),bg="#e0ffff").place(x=20,y=190)
	sublabel5=Label(mGUI,text="Question 2",font=(None,12),bg="#e0ffff").place(x=20,y=230)
	sublabel6=Label(mGUI,text="Answer",font=(None,12),bg="#e0ffff").place(x=20,y=270)
	sublabel7=Label(mGUI,text="Question 3",font=(None,12),bg="#e0ffff").place(x=20,y=310)
	sublabel8=Label(mGUI,text="Answer",font=(None,12),bg="#e0ffff").place(x=20,y=350)
	entry3=Entry(mGUI,textvariable=q1,font=(None,11),width=17).place(x=200,y=150)	
	entry4=Entry(mGUI,textvariable=a1,font=(None,11),width=17,show="*").place(x=200,y=190)	
	entry5=Entry(mGUI,textvariable=q2,font=(None,11),width=17).place(x=200,y=230)	
	entry6=Entry(mGUI,textvariable=a2,font=(None,11),width=17,show="*").place(x=200,y=270)	
	entry7=Entry(mGUI,textvariable=q3,font=(None,11),width=17).place(x=200,y=310)	
	entry8=Entry(mGUI,textvariable=a3,font=(None,11),width=17,show="*").place(x=200,y=350)	
	
	savebutton=Button(mGUI,text="Save",font=(None,12),command=lambda:storedata(root,passwd,mGUI,q1,a1,q2,a2,q3,a3)).place(x=160,y=390)
	
	mGUI.mainloop()
	

def updatemaster(masterpwd,mainGUI):

	"""
	GUI for modifying master password
	"""

	mGUI=Toplevel()
	mGUI.wm_iconbitmap(bitmap="@LoginAT_logo.xbm")
	mGUI.title("Password Manager")
	border=Canvas(mGUI,width=400,height=250)
	border.pack()
	border.create_rectangle(6,6,394,50,width=0, fill="#e0ffff")
	border.create_rectangle(6,56,394,234,width=0, fill="#e0ffff")	
	mGUI.geometry("400x240")
	mGUI.resizable(width=False,height=False)		
	old=StringVar()
	new=StringVar()
	root=StringVar()
	toplabel=Label(mGUI,text="Change Master Password",font=(None,14,"bold"),bg="#e0ffff").place(x=50,y=15)	
	sublabel1=Label(mGUI,text="Old Password",font=(None,12),bg="#e0ffff").place(x=20,y=70)
	entry1=Entry(mGUI,textvariable=old,font=(None,11),width=20,show="*")
	entry1.place(x=170,y=70)	
	entry2=Entry(mGUI,textvariable=new,font=(None,11),width=20,show="*")
	entry2.place(x=170,y=110)	
	sublabel2=Label(mGUI,text="New Password",font=(None,12),bg="#e0ffff").place(x=20,y=110)
	sublabel3=Label(mGUI,text="Root Password",font=(None,12),bg="#e0ffff").place(x=20,y=150)
	entry3=Entry(mGUI,textvariable=root,font=(None,11),width=20,show="*")
	entry3.place(x=170,y=150)	
	savebutton=Button(mGUI,text="Save",font=(None,12),command=lambda:changedata(root,old,new,mGUI,entry1,entry2,entry3,mainGUI)).place(x=160,y=190)
	
if(__name__=="__main__"):
	pass

	# test the module here

	

