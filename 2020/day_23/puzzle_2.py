import itertools
from pprint import pprint
import numpy as np
from copy import deepcopy
import operator
import re
from tqdm import tqdm

def get_destination(current_cup, next_3, max_cup_num):
	dest = current_cup-1
	while dest == 0 or dest in next_3:
		if dest == 0: 
			dest = max_cup_num
		if dest in next_3:
			dest -= 1
	return dest

def step(cup_dict, current_cup, max_cup_num):
	n1 = cup_dict[current_cup]
	n2 = cup_dict[n1]
	n3 = cup_dict[n2]
	next_3 = [n1,n2,n3]
	dest = get_destination(current_cup, next_3, max_cup_num)
	cup_dict[current_cup] = cup_dict[n3]
	cup_dict[n3] = cup_dict[dest]
	cup_dict[dest] = n1
	return cup_dict, cup_dict[current_cup]

def get_answer(cup_dict):
	n1 = cup_dict[1]
	n2 = cup_dict[n1]
	return n1*n2

with open("data.txt") as data:
	lines = data.read().splitlines()
cups = list(map(int, [x for x in lines[0]]))
max_cup_num = 10**6
cups = cups + list(range(10,max_cup_num+1))

cup_dict = {cups[ii]: cups[ii+1] for ii in range(len(cups)-1)}
cup_dict[cups[-1]] = cups[0]
current_cup = cups[0]
for ii in range(10**7):
	cup_dict, current_cup = step(cup_dict, current_cup, max_cup_num)

print("Answer:",get_answer(cup_dict))

# Answer: 680435423892