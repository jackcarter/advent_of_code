import itertools
from pprint import pprint
import numpy as np
from copy import deepcopy
import operator

def get_matching_close_paren(section, start):
	paren_stack = 0
	for ii, char in enumerate(section):
		if ii < start:
			continue
		if char == '(':
			paren_stack += 1
		elif char == ')':
			paren_stack -= 1
		if paren_stack == 0:
			return ii

def evaluate_minimal(expression):
	lookup = {'+': operator.add, '*': operator.mul}
	return lookup[expression[1]](int(expression[0]), int(expression[2]))

def evaluate_no_parens(expression):
	expression = expression.split(" ")
	while len(expression) > 1:
		intermediate_result = evaluate_minimal(expression[:3])
		expression = [intermediate_result] + expression[3:]
	return intermediate_result
	
def evaluate(section):
	if '(' in section:
		for ii, char in enumerate(section):
			if char == '(':
				matching_close_paren = get_matching_close_paren(section, ii)
				inside_parens = evaluate(section[ii+1:matching_close_paren])
				return evaluate(section[:ii] + str(inside_parens) + section[matching_close_paren+1:])
	else:
		return evaluate_no_parens(section)
		

with open("data.txt") as data:
	lines = data.read().splitlines()

print("Answer:",sum([evaluate(line) for line in lines]))

# Answer: 45283905029161