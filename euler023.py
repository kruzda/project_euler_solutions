#!/usr/bin/env python3

"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

# the commented out fields are my firs solution. using that took 36 minutes to get the result. the few lines that replace it (a solution posted in the forum) take around 9 seconds.

#from bisect import bisect
import math


"""
abundant_numbers = []
def init():
	for a in range(12, 28125):
		if a < dd(a):
			abundant_numbers.append(a)
"""

def dd(n):
	result = [1]
	for d in range(2, int(math.sqrt(n))+1):
		div = n % d
		if div == 0:
			result += [a for a in [int(n/d)] if not a in result]
			result += [a for a in [d] if not a in result]
	return(sum(result))

"""
def suitable(n):
	for ab in abundant_numbers[bisect(abundant_numbers, n-12)-1::-1]:
		if n - ab in abundant_numbers:
			print("unsuitable: {}. ( {} - {} = {} (which is an abundant number))".format(n, n, ab, n-ab))
			return False
	print("suitable: {}.".format(n))
	return True
"""

def abundantsum(i):
	return(any(i-a in abundant_numbers for a in abundant_numbers))

def main():
	return(sum(i for i in range(1,28124) if not abundantsum(i)))
"""
	results = []
	for x in range(28123, 0, -1):
		if (12 < x and not x % 2) or suitable(x):
			results.append(x)
	return(sum(results))
"""

if __name__ == "__main__":
	#init()
	abundant_numbers = set(i for i in range(1,28124) if i < dd(i))
	print("working with {} abundant numbers".format(len(abundant_numbers)))
	print("result: {}".format(main()))
