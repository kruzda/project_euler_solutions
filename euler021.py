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
	for d in range(2, int(math.sqrt(n))+1):
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
	return(result)

def main():
	sum = 0
	for a in range(1, 10000):
		b = d(a)
		if a != b and a == d(b):
			sum += a

	print(sum)

if __name__ == "__main__":
	main()
