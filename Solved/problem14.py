def Collatzlenght(number):
    if number==1:
        return 1
    if number%2==0:
        number=number/2
    else:
        number=number*3+1
    return Collatzlenght(number)+1


record=0

for i in range(1,1000000):
    curcollatz=Collatzlenght(i)
    if curcollatz>record:
        record=curcollatz
        print "Got a new record!",i,"with a lenght of",curcollatz
