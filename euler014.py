#!/usr/bin/python

max_length = 0

for i in range(1, 1000000):
    chain=[i]
    n = 0
    while i != 1:
        if not i % 2:
            i = i / 2
        else:
            i = 3 * i + 1
        chain.append(i)
    if max_length < len(chain):
        max_length = len(chain)
        print(chain, max_length)

