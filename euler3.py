#!/usr/bin/python

'''
https://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

import time
import math

start_time=time.time()

def isprime(n, i):
    m = math.sqrt(n)
    if m.is_integer() or not n % 2:
        return False
    while i<m:
        if not n % i:
            return False
        i+=1
    return True

d=2
j=13195
j=600851475143
# j=317584931803

while 1 < j:
    if not j % d:
        j = j / d
        d = d - 1;
    d = d + 1

print(d)

# while d!=j:
    # if not d % 1000000:
        # loops_per_second = int(d/(time.time() - start_time))
        # eta = (j - d) // loops_per_second
        # print("{} {}/s ETA: {}".format(d, loops_per_second, eta))
    # if isprime(d, 2) and not j % d:
        # print("p: {}".format(d))
    # d+=1
