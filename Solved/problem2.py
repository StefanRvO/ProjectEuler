#!/usr/bin/python

this=1
prev=0
preprev=0

recursions=1
summe=0
while(len(str(this))<1000):
	preprev=prev
	prev=this
	this=prev+preprev
	recursions+=1
	if this>4000000:
	    break
	if this%2==0:
		summe+=this
print summe

