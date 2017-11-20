#!/usr/bin/python

myset=[1,2]
while myset[-1] + myset[-2] <= 4000000:
    myset.append(myset[-1] + myset[-2])

print(myset)
print(sum(i for i in myset if not i % 2))
