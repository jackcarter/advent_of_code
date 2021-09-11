import itertools
from pprint import pprint
import numpy as np
from copy import deepcopy
import operator
import re

def get_next_3(cups):
	return cups[1:4]

def get_destination(cups, next_3):
	dest = cups[0]-1
	while dest == 0 or dest in next_3:
		if dest == 0: 
			dest = 9
		if dest in next_3:
			dest -= 1
	return dest

def move_cups(cups, destination):
	di = cups.index(destination)
	return [cups[0]] + cups[4:di+1] + cups[1:4] + cups[di+1:]

def update_current(cups):
	return cups[1:] + [cups[0]]

def step(cups):
	#assume that current is always first in the list
	current = cups[0]
	next_3 = get_next_3(cups)
	destination = get_destination(cups, next_3)
	cups = move_cups(cups, destination)
	cups = update_current(cups)
	return cups

def get_cups_after_1(cups):
	i1 = cups.index(1)
	cups_after_1 = cups[i1+1:] + cups[:i1]
	return "".join(list(map(str,cups_after_1)))

with open("data.txt") as data:
	lines = data.read().splitlines()

cups = list(map(int, [x for x in lines[0]]))

for ii in range(100):
	cups = step(cups)

print("Answer:",get_cups_after_1(cups))

# Answer: 29385746