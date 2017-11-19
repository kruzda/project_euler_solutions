#!/bin/bash

from itertools import permutations

for route in permutations(['right', 'down']):
    print(route)
