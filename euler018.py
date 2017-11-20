#!/usr/bin/python3
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('lookahead', type=int)


pyramid=[]
pyramid.append([75])
pyramid.append([95,64])
pyramid.append([17,47,82])
pyramid.append([18,35,87,10])
pyramid.append([20,4,82,47,65])
pyramid.append([19,1,23,75,3,34])
pyramid.append([88,2,77,73,7,63,67])
pyramid.append([99,65,4,28,6,16,70,92])
pyramid.append([41,41,26,56,83,40,80,70,33])
pyramid.append([41,48,72,33,47,32,37,16,94,29])
pyramid.append([53,71,44,65,25,43,91,52,97,51,14])
pyramid.append([70,11,33,28,77,73,17,78,39,68,17,57])
pyramid.append([91,71,52,38,17,14,91,43,58,50,27,29,48])
pyramid.append([63,66,4,68,89,53,67,30,73,16,69,87,40,31])
pyramid.append([4,62,98,27,23,9,70,98,73,93,38,53,60,4,23])

"""
pyramid=[]
pyramid.append([3])
pyramid.append([7, 4])
pyramid.append([2, 4, 6])
pyramid.append([8, 5, 9, 3])
"""

parser.set_defaults(lookahead=len(pyramid))

args = parser.parse_args()

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

max_path_sum = 0
selected_element_index = 0
output = ""
for v_pos, this_row in enumerate(pyramid):
    first_sum_potential = sum(map(sum, [x[selected_element_index:selected_element_index+i+1] for i,x in enumerate(pyramid[v_pos:v_pos+args.lookahead])]))
    second_sum_potential = sum(map(sum, [x[selected_element_index+1:selected_element_index+i+2] for i,x in enumerate(pyramid[v_pos:v_pos+args.lookahead])]))
    if first_sum_potential < second_sum_potential and len(this_row):
        selected_element_index += 1
    for i,e in enumerate(this_row):
        if e < 10:
            e = "0" + str(e)
        if i == selected_element_index:
            output += color.BOLD + str(e) + color.END
        else:
            output += str(e)
        if i != len(this_row):
            output += " "
    print("{:^{}}".format(output, 60))
    output = ""
    max_path_sum += this_row[selected_element_index]
  

print("max_path_sum: {}, height: {}".format(max_path_sum, len(pyramid)))