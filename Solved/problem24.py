#!/usr/bin/python
from itertools import permutations

listen=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

permu=list(permutations(listen))

permu.sort()

lol= permu[999999]

string=''

for i in lol:
    string+=str(i)

print string
