#!/usr/bin/python

j = k = 0
for i in range(1,101):
	j += i
	k += i ** 2

j = j ** 2

print(j-k)

