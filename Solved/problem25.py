#!/usr/bin/python

this=1
prev=0
preprev=0

recursions=1

while(len(str(this))<1000):
	preprev=prev
	prev=this
	this=prev+preprev
	recursions+=1
print recursions,":",this,"Digits:",len(str(this)),"\n\n"

