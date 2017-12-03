#!/usr/bin/python3

"""
Project Euler problem #021

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

def divisors(n):
	result = []
	for d in range(1, n//2+1):
		if not n % d:
			result.append(d)
	return(result)

amicable = []
for i in range(10001):
	di_a = divisors(i)
	sd_a = sum(di_a)
	di_b = divisors(sd_a)
	sd_b = sum(di_b)
	if i == sd_b and sd_a != sd_b and [sd_b, sd_a] not in amicable:
		amicable.append([sd_a, sd_b])

print(sum(map(sum, (x for x in amicable))))
