#!/usr/bin/python

def ispal(n):
	return int(str(n)[::-1])==n
results=[]

"""
for i in range(100,999):
	for j in range(100,999):
		if ispal(i*j):
			results.append(i*j)

results.sort()
print(results[-1])
"""

"""
palindrome algebra:
abccba
100000a + 10000b + 1000c + 100c + 10b + a
100001a + 10010b + 1100c

11(9091a + 910b + 100c)

"""
max = maxI = maxJ = 0
i=999
j=999

while(100<i):
	j = 990
	while(100<j):
		product = i*j
		if (max < product and ispal(product)):
			max = product
			maxI= i
			maxJ= j	
		j-=11
	i-=1
print("max: {} maxI: {} maxJ: {}".format(max, maxI, maxJ))
