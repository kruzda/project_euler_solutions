#!/usr/bin/python

import math
import time

def triangle(n):
	t = 0
	for i in range(n+1):
		t += i
	return t

def fractions(n):
	if n != 1:
		f = [1, n]
	else:
		return [1]
	ff = 2
	i = n // ff
	smallest_known_divisor = 1
	while smallest_known_divisor < i:
		if n % i == 0:
			f.append(i)
			f.append(ff)
			smallest_known_divisor = ff
		ff += 1
		i = n // ff
	return set(f)

g = 0
start_time = time.time();

for i in range(1, 111111):
	tr = triangle(i)
	fr = fractions(tr)
	if g < len(fr):
		print("{}->{} ({}) {}".format(i, tr, len(fr), int(time.time() - start_time)))
		g = len(fr)
