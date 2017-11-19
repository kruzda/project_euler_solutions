#!/usr/bin/python
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--x', type=int)
parser.add_argument('--search', type=int)
parser.add_argument('--verbose', action="store_true")
parser.set_defaults(x=10, search=2520)

args = parser.parse_args()

x=range(1,args.x+1)
y=range(1,args.search+1,1)

r=[]

def dprint(*text):
    if args.verbose:
        print(text)

dprint(x)

def decide(arr, ci, p):
    try:
        for m in range(len(y)):
            dprint(1, arr[ci],y[m], ci)
            p2 = arr[ci]*y[m]
            if p < p2:
                # if the next product is larger even when multiplied by 1 then the current product can be excluded from the possible values
                dprint("{}<{} - larger, returning with False".format(p,p2))
                return False
            if p2 < p:
                # if the next product is smaller try to see how big it can be by multiplying it with the next y
                dprint("{}<{} - smaller, continuing".format(p2,p))
                continue
            if p == p2:
                # if the next product is the same as the current product then try to see the next next product
                dprint("{}={} - so it's the same".format(p, p2))
                dprint("r={}".format(r))
                r.append(p2)
                dprint("recursing. arr={}, ci+1={}, p2={}, r={}".format(arr, ci+1, p2, r))
                return decide(arr, ci+1, p2)
    except IndexError:
        return True

for l in range(len(x)):
    for m in range(len(y)):
        r=[]
        p = x[l]*y[m]
        dprint(0, x[l],y[m], l)
        dprint("calling decide with: x={}, l+1={}, p={}".format(x, l+1, p))
        if decide(x, l+1, p):
            print("found: {}".format(p))
            sys.exit(0)
