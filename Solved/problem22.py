letters='abcdefghijklmnopqrstuvwxyz'

file=open('names.txt')

names=file.read()

names=names.split(',')

for i in range(len(names)):
    names[i]=names[i][1:-1]


names.sort()


namesvalues=[]
totsum=0
for name in names:
    placement=names.index(name)+1
    summe=0
    for char in name.lower():
        summe+=letters.index(char)+1
    totsum+=placement*summe
print totsum
