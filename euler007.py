#!/usr/bin/python
import math
"""
project euler problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?


"""

def isprime(n):
	if n <= 1:
		return False
	if n % 2 == 0 and n != 2:
		return False
	for r in range(3, int(math.sqrt(n) + 1)):
		if n % r == 0:
			return False
	return True

def main():
	n = 0
	nth_prime = 1
	while nth_prime < 10002:
		if isprime(n):
			print(nth_prime, n)
			nth_prime+=1
		n+=1

if __name__=="__main__":
	main()

