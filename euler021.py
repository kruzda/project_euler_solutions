#!/usr/bin/python3
import math # quick maths

"""
Project Euler problem #021

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

# optimisation ideas from the thread
def d(n):
	result = 1
	square = math.sqrt(n)
	for d in range(2, int(math.sqrt(n))):
		div = n % d
		if div == 0:
			result += d
			result += int(n / d)
	return(result)

def divisors(n):
	result = []
	for d in range(1, n//2+1):
		if not n % d:
			result.append(d)
	return(sum(result))

amicable = []
for i in range(10001):
	sd_a = d(i)
	sd_b = d(sd_a)
	if i == sd_b and sd_a != sd_b and [sd_b, sd_a] not in amicable:
		amicable.append([sd_a, sd_b])

print(sum(map(sum, (x for x in amicable))))
