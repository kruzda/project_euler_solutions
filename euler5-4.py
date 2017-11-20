#!/usr/bin/python
import math

k = 20
N = 1
i = 1
p = [2, 3, 5, 7, 11, 13, 17, 19]
a = []
check = True
limit = math.sqrt(k)
while p[i] <= k:
	if check:
		if p[i] <=limit:
			a.append(math.floor(math.log(k) / math.log(p[i])))
		else:
			check = False
	N = N * p[i] ** a[i]
	i += 1

print(N)
