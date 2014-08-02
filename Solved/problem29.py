
liste=[]

for a in range(2,101):
    for b in range(2,101):
        liste.append(a**b)

print len(list(set(liste)))
