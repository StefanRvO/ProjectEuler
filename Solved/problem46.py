#!/usr/bin/python
from gmpy2 import *
get_context().precision=1000
a=mpfr(7.)
b=mpfr(1.)
print str(div(b,a))[2:]
