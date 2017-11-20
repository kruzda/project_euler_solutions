#!/usr/bin/python
import math
import argparse

'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

parser = argparse.ArgumentParser(prog='euler3.py')
parser.add_argument("n", type=int, help='the number to factor')
args = parser.parse_args()
n = args.n

if n % 2 == 0:
	lastfactor = 2
	n /= 2
	while n % 2 == 0:
		n /= 2
else:
	lastfactor = 1

factor = 3
maxfactor=math.sqrt(n)

while 1 < n and factor <= maxfactor:
	if n % factor == 0:
		print("{} is a prime factor of {}. it fits {} times".format(factor, n, n / factor))
		n /= factor
		lastfactor = factor
		while not n % factor:
			n /= factor
			print("{} fits {} times to it".format(factor, n))
		maxfactor = math.sqrt(n)
	factor += 2

if n == 1:
	print(lastfactor)
else:
	print(n)
