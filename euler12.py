#!/usr/bin/python
import math

def triangle(n):
    r = 0
    for i in range(1, n+1):
        r += i
    return r

def factors(n):
    # everything is divisible by 1 and itself, so start from 2 factors
    f = 2
    divisor = 2
    while divisor < n:
        if not n % divisor:
            f += 1
        divisor += 1
    return f

greatest_number_of_factors = 0

for i in range(1,111111):
    tr = triangle(i);
    fr = factors(tr);
    if greatest_number_of_factors < fr:
        print("{}: {}".format(tr, fr))
        greatest_number_of_factors = fr
