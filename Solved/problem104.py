#!/usr/bin/python
def isPandigital(string):
    if sorted(string)==['1','2','3','4','5','6','7','8','9']:
        return True
    return False

def doublePandigital(number):
    if isPandigital(str(number%1000000000))  and isPandigital(str(number)[:9]):
        return True
class fibio:
    """fibionacy generator class"""
    switch=True
    F1=0
    F2=0
    generation=0
    def __init__(self,fibionum=1,gen=1):
        self.F2=fibionum
        self.generation=gen
    def next(self):
        self.switch=not(self.switch)
        self.generation+=1
        if self.switch:
            self.F2=self.F2+self.F1
            return self.F2
        else:
            self.F1=self.F2+self.F1
            return self.F1
    def cur(self):
        if self.switch:
            return self.F2
        else:
            return self.F1
            

j=fibio()
while True:
    if doublePandigital(j.next()):
        break
print  j.generation
