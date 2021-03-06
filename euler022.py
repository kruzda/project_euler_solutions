#!/usr/bin/python3

"""
Project Euler #022

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order.
Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

"""

f = open("/home/k/p022_names.txt").read().split(',')
fi = list(map(lambda s: s.strip('"'), f))
fis = sorted(fi)

def value(name):
	sum = 0
	for letter in name:
		sum += ord(letter) - 64
	return(sum)

sum = 0
for i in range(len(fis)):
	score = value(fis[i]) * (i + 1)
	sum += score
		
print(sum)

