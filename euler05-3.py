#!/usr/bin/python

i = 1
for k in range(1, 21):
	if 0 < i % k:
		for j in range(1, 21):
			if (i*j) % k == 0:
				i *= j
				break
print i
