#!/usr/bin/python
from itertools import permutations
import sys

cubes=[]
cubesortedstrings=[]
#Create cubes
for i in range(2,20000):
    cubes.append(i**3)
    cubesortedstrings.append(sorted(str(i**3)))

maxcubes=0
for cube in cubes:
    permcubes=cubesortedstrings.count(sorted(str(cube)))
    if permcubes>maxcubes:
        print "New record",cube,"with", permcubes,"cubic permutations."
        maxcubes=permcubes
