#!/usr/bin/python3
import argparse

parser = argparse.ArgumentParser(prog='euler17.py')
parser.add_argument("n1", type=int, help='start of range')
parser.add_argument("n2", type=int, help='end of range')
args = parser.parse_args()

d = {	1: "one",
		2: "two",
		3: "three",
		4: "four",
		5: "five",
		6: "six",
		7: "seven",
		8: "eight",
		9: "nine",
		10: "ten",
		11: "eleven",
		12: "twelve",
		13: "thirteen",
		15: "fifteen",
		18: "eighteen",
		20:	"twenty",
		30: "thirty",
		40: "forty",
	    50: "fifty",	
		80: "eighty",
		100: "hundred",	
		1000: "thousand"
	}


def print_numbers_as_letters(n):
	result = ""
	i = n
	y = len(d)
	while 0 < i and 0 < y:
		dd = max(sorted(d)[:y])
		if dd <= i:
			if 1000 <= dd:
				multiples_of_thousand = i // 1000
				i -= multiples_of_thousand * 1000
				if 0 < i <= 100:
					filler = "and"
				else:
					filler = ""
				result += d[multiples_of_thousand] + d[1000] + filler
			elif 100 <= dd:
				multiples_of_hundred = i // 100
				i -= multiples_of_hundred * 100
				if i != 0:
					filler = "and"
				else:
					filler = ""
				result += d[multiples_of_hundred] + d[100] + filler
			elif 20 <= dd:
				multiples_of_ten = i // 10
				if not multiples_of_ten * 10 in d.keys():
					result += d[multiples_of_ten] + "ty"
				else:
					result += d[multiples_of_ten * 10]
				i -= multiples_of_ten * 10
			else:
				if i < 20 and not i in d.keys():
					result += d[i-10] + "teen"
					i = 0
				else:
					result += d[dd]
					i -= dd
		else:
			y -= 1
	return(result)

n1 = args.n1
n2 = args.n2
l = 0
for i in range(n1, n2+1):
	the_number = print_numbers_as_letters(i)
	print(the_number)
	l += len(the_number)
print("final length: {}".format(l))

