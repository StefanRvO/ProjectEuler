#!/usr/bin/python
count=0

for i in xrange((200/1)+1):
    print i
    for j in xrange((200/2)+1):
        if i+2*j>200:
            break
        for k in xrange((200/5)+1):
            if i+2*j+5*k>200:
                break
            for l in xrange((200/10)+1):
                if i+2*j+5*k+10*l>200:
                    break
                for m in xrange((200/20)+1):
                    if i+2*j+5*k+10*l+20*m>200:
                        break
                    for n in xrange((200/50)+1):
                        if i+2*j+5*k+10*l+20*m+50*n>200:
                            break
                        for o in xrange((200/100)+1):
                            if i+2*j+5*k+10*l+20*m+50*n+100*o>200:
                                break
                            for p in xrange(2):
                                if i+2*j+5*k+10*l+20*m+50*n+100*o+p*200==200:
                                    count+=1
print count
                                    
                            
