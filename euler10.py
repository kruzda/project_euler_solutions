#!/usr/bin/python
import math

primesum = 2
r = 2000000
i = 3

def isprime(i):
    for j in range(3, int(math.sqrt(i))+1):
        if not i % j:
            return False
    return True

while i < r:
    if isprime(i):
        primesum += i
    i += 2

print(primesum)
