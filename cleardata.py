# cleardata.py
# Author: Nihesh Anderson K
# 3 Sept 2016

import sys
from tkinter import *
import os
import string
from login import pad
from Crypto.Cipher import AES
import base64

directory=""
directory2=""

"""
This module is used to remove previously stored passwords 
"""

def forgetdata(num,subGUI,i,count,masterpwd):

	"""
	Function for erasing ith data from a certain category
	"""
	
	list=[]
	string=""
	flag=0
	file=open(directory+"settings.txt","r")
	file2=open(directory+"temp.txt","w")
	j=1
	for line in file:
		if(num==j and line!="\n"):
			line=line.rstrip("\n")
			line=int(line)
			while(line>0):
				list.append(line%10)
				line=line//10
			list.sort()
			for val in list:
				if(flag==0 and val!=i):
					string=string+str(val)
				elif val==i:
					flag=1
				else:
					string=string+str(val-1)
			file2.write(string+"\n")
		else:
			file2.write(line)
		j+=1
	file.close()
	file2.close()
	os.remove(directory+"settings.txt")
	os.rename(directory+"temp.txt",directory+"settings.txt")

	j=1
	newfile=open(directory+"temp.txt","w")
	os.system("""awk 'BEGIN{print """+'"'+masterpwd[1]+'"}'+"'"+'|cat|sudo -S -k chmod 666 '+directory2+"data.txt")
	with open(directory+"data.txt","r+") as file:
		for line in file:		
			if(j==num):
				if(count==1):
					newfile.write("user pass\n")
				else:
					start=0
					end=line.find(" ")
					end=line.find(" ",end+1)
					for n in range(i-1):
						if(n==count-1):
							break
						start=end+1
						end=line.find(" ",start)
						end=line.find(" ",end)
					if(i==count):
						text=line[:end]+"\n"
					else:
						text=line[:start]+line[end+1:]
					newfile.write(text)
						 
			else:
				newfile.write(line)
			j+=1
	os.remove(directory+"data.txt")
	os.rename(directory+"temp.txt",directory+"data.txt")
	newfile.close()
	os.system("""awk 'BEGIN{print """+'"'+masterpwd[1]+'"}'+"'"+'|cat|sudo -S -k chown root:root '+directory2+"data.txt")
	os.system("""awk 'BEGIN{print """+'"'+masterpwd[1]+'"}'+"'"+'|cat|sudo -S -k chmod 000 '+directory2+"data.txt")
	
	subGUI.destroy()

def accounts(num,masterpwd): 

	"""
	Creates a GUI alert box, asking the user to confirm deletion
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

	if(data[:data.find(" ")]=="user"):
		subGUI.title("Alert")
		subGUI.geometry("400x100")
		border=Canvas(subGUI,width=400,height=100)
		border.pack()
		border.create_rectangle(6,6,394,94,width=0, fill="#7FFFD4")
		subGUI.resizable(width=False,height=False)
		QLabel1=Label(subGUI,text="Credentials have not been set",font=(None,13,"bold"),bg="#7FFFD4").place(x=32,y=40)

	else:
		subGUI.title(titlebox)
		subGUI.geometry("500x"+str((60*count)+40))
		border=Canvas(subGUI,width=500,height=(60*count)+40)
		border.pack()
		border.create_rectangle(6,6,494,(60*count)+34,width=0, fill="#7FFFD4")
		subGUI.resizable(width=False,height=False)
		label1=[None]*count
		buttondel=[None]*count
		aes=AES.new(pad(masterpwd[0]))
	
		start=0
		end=data.find(" ")	
		for i in range(count):
			user=data[start:end]		
			user=aes.decrypt(base64.b64decode(user.encode()))
			user=user.decode("utf-8")
			user=user.rstrip("{")
			border.create_rectangle(6,31+(60*i),494,77+(60*i),width=0, fill="#E0FFFF")
			label1[i]=Label(subGUI,text=user,font=(None,13),bg="#E0FFFF").place(x=30,y=42+(60*i))
			buttondel[i]=Button(subGUI,text="Delete",command=lambda:forgetdata(num,subGUI,i,count,masterpwd),font=(None,13),padx=5,pady=5).place(x=390,y=35+(60*i))
			if(i!=count-1):
				temp=start
				start=(data.find(" ",end+1))+1
				end=data.find(" ",start+1)

if(__name__=="__main__"):
	pass

	# test the module here
