#!/usr/bin/python3

"""
Project Euler problem #019

You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

def is_a_leap_year(year):
	return(bool(not year % 4 and year % 100 or (not year % 100 and not year % 400)))

num_days = { 1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31 }

day = 366
sundays_on_the_first = 0

for year in range(1901, 2001):
	if is_a_leap_year(year):
		num_days[2] = 29
	else:
		num_days[2] = 28
	for m in num_days:
			day += num_days[m]
			if not day % 7:
				sundays_on_the_first += 1

print(sundays_on_the_first)

"""
or just 1200/7 = 171
there are 1200 months in 100 years
which makes 1200 1st days of the month
approximate answer but over this span of time there is enough regularity
"""
