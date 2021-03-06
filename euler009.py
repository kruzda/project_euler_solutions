#!/usr/bin/python
import math

"""

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a**2 + b**2 = c**2

For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""
	
for a in range(500):
	pa = a**2
	for b in range(500):
		pb = b**2
		pc = pa + pb
		c = math.sqrt(pc)
		if a + b + c == 1000 and a < b < c:
			c = int(c)
			print("{}**2 + {}**2 = {}**2".format(a, b, c))
			print("{} + {} = {}".format(pa, pb, pc))
			print("{} + {} + {} = {}".format(a, b, c, a+b+c))
			print("{} * {} * {} = {}".format(a, b, c, a*b*c))

