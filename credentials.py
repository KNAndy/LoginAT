# credentials.py
# Author: Nihesh Anderson K
# 2 Oct 2016

import sys
from tkinter import *
import os
import string
from Crypto.Cipher import AES
from hashlib import md5
import base64

directory=""
directory2=""

"""
This module is used to seek credentials from the user for various websites
"""

def dialog(subGUI,title,xcoord,num,masterpwd):

	"""
	Function for the standard dialog box for credential modification
	"""

	subGUI.title("Sign In")
	border=Canvas(subGUI,width=400,height=200)
	border.pack()
	border.create_rectangle(6,6,394,50,width=0, fill="#e0ffff")
	border.create_rectangle(6,56,394,194,width=0, fill="#e0ffff")	
	subGUI.geometry("400x200")
	subGUI.resizable(width=False,height=False)
	usercontent=StringVar()
	passwdcontent=StringVar()
	userlabel=Label(subGUI,text="Username",font=(None,11),bg="#e0ffff").place(x=50,y=67)
	passwdlabel=Label(subGUI,text="Password",font=(None,11),bg="#e0ffff").place(x=50,y=102)
	userentry=Entry(subGUI,textvariable=usercontent,font=(None,11),width=20).place(x=150,y=65)
	passwdentry=Entry(subGUI,textvariable=passwdcontent,font=(None,11),width=20,show="*").place(x=150,y=100)
	savebutton=Button(subGUI,text="save",font=(None,16),command=lambda:feed(usercontent,passwdcontent,num,subGUI,masterpwd)).place(x=190,y=150)
	label=Label(subGUI,text=title,font=(None,16,"bold"),bg="#e0ffff").place(x=xcoord,y=15)

def pad(text):

	"""
	Pads with { to convert the string into 32 characters
	"""

	return text+("{"*(32-len(text)))

def feed(usercontent,passwdcontent,num,subGUI,masterpwd):

	"""
	Function for feeding new credentials into the text file
	"""

	aes=AES.new(pad(masterpwd[0]))
	user=usercontent.get()
	passwd=passwdcontent.get()
	user=aes.encrypt(pad(user).encode())
	user=base64.b64encode(user)
	user=user.decode()
	passwd=aes.encrypt(pad(passwd).encode())
	passwd=base64.b64encode(passwd)
	passwd=passwd.decode()	
	null=aes.encrypt(pad("").encode())
	null=base64.b64encode(null)
	null=null.decode()
	i=1
	newfile=open(directory+"temp.txt","w")
	os.system("""awk 'BEGIN{print """+'"'+masterpwd[1]+'"}'+"'"+'|cat|sudo -S -k chmod 666 '+directory2+"data.txt")
	with open(directory+"data.txt","r") as file:
		for line in file:		
			if(i==num):
				line=line.strip("\n")				
				usrid=line[:line.find(" ")]
				usrpass=line[line.find(" ")+1:]
				if(usrid=="user" and usrpass=="pass"):
					newfile.write(user+" "+passwd+"\n")
				elif((user!=usrid or passwd!=usrpass) and user!=null and passwd!=null):
					newfile.write(line+" "+user+" "+passwd+"\n")
				else:
					newfile.write(line+"\n")
			else:
				newfile.write(line)
			i+=1
	os.remove(directory+"data.txt")
	os.rename(directory+"temp.txt",directory+"data.txt")
	newfile.close()
	os.system("""awk 'BEGIN{print """+'"'+masterpwd[1]+'"}'+"'"+'|cat|sudo -S -k chown root:root '+directory2+"data.txt")
	os.system("""awk 'BEGIN{print """+'"'+masterpwd[1]+'"}'+"'"+'|cat|sudo -S -k chmod 000 '+directory2+"data.txt")
	
	subGUI.destroy()
	
def seekfblogin(masterpwd):

	"""
	Function for modifying facebook credentials
	"""

	subGUI=Toplevel()
	subGUI.wm_iconbitmap(bitmap="@LoginAT_logo.xbm")
	dialog(subGUI,"Facebook",140,1,masterpwd)
	imagesrc=PhotoImage(file=directory+"facebook.png")
	imagesrc=imagesrc.subsample(9,9)
	savelabel=Label(subGUI,image=imagesrc).place(x=150,y=150)
	subGUI.mainloop()

def seektwitterlogin(masterpwd):

	"""
	Function for modifying twitter credentials
	"""

	subGUI=Toplevel()
	subGUI.wm_iconbitmap(bitmap="@LoginAT_logo.xbm")
	dialog(subGUI,"Twitter",150,2,masterpwd)
	imagesrc=PhotoImage(file=directory+"twitter.png")
	imagesrc=imagesrc.subsample(9,9)
	savelabel=Label(subGUI,image=imagesrc).place(x=150,y=150)
	subGUI.mainloop()

def seekbackpacklogin(masterpwd):

	"""
	Function for modifying backpack credentials
	"""

	subGUI=Toplevel()
	subGUI.wm_iconbitmap(bitmap="@LoginAT_logo.xbm")
	dialog(subGUI,"Backpack",140,3,masterpwd)
	imagesrc=PhotoImage(file=directory+"backpack.png")
	imagesrc=imagesrc.subsample(9,9)
	savelabel=Label(subGUI,image=imagesrc).place(x=150,y=150)
	subGUI.mainloop()

def seekinstalogin(masterpwd):

	"""
	Function for modifying instagram credentials
	"""

	subGUI=Toplevel()
	dialog(subGUI,"Instagram",135,4,masterpwd)
	imagesrc=PhotoImage(file=directory+"insta.png")
	imagesrc=imagesrc.subsample(9,9)
	savelabel=Label(subGUI,image=imagesrc).place(x=150,y=150)
	subGUI.mainloop()

def seekgmaillogin(masterpwd):

	"""
	Function for modifying gmail credentials
	"""

	subGUI=Toplevel()
	subGUI.wm_iconbitmap(bitmap="@LoginAT_logo.xbm")
	dialog(subGUI,"Gmail",165,5,masterpwd)
	imagesrc=PhotoImage(file=directory+"gmail.png")
	imagesrc=imagesrc.subsample(9,9)
	savelabel=Label(subGUI,image=imagesrc).place(x=150,y=150)
	subGUI.mainloop()

def seekdrivelogin(masterpwd):

	"""
	Function for modifying drive credentials
	"""

	subGUI=Toplevel()
	subGUI.wm_iconbitmap(bitmap="@LoginAT_logo.xbm")
	dialog(subGUI,"Drive",165,7,masterpwd)
	imagesrc=PhotoImage(file=directory+"drive.png")
	imagesrc=imagesrc.subsample(9,9)
	savelabel=Label(subGUI,image=imagesrc).place(x=150,y=150)
	subGUI.mainloop()

def seekyoutubelogin(masterpwd):

	"""
	Function for modifying youtube credentials
	"""

	subGUI=Toplevel()
	subGUI.wm_iconbitmap(bitmap="@LoginAT_logo.xbm")
	dialog(subGUI,"Youtube",145,8,masterpwd)
	imagesrc=PhotoImage(file=directory+"youtube.png")
	imagesrc=imagesrc.subsample(9,9)
	savelabel=Label(subGUI,image=imagesrc).place(x=150,y=150)
	subGUI.mainloop()

if(__name__=="__main__"):
	pass
		
	# test the module here


