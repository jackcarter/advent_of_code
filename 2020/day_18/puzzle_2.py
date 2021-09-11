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

def remove_one(expression, op):
	lookup = {'+': operator.add, '*': operator.mul}
	func = lookup[op]
	ind = expression.index(op)
	new_expression = expression[:ind-1] + [func(int(expression[ind-1]), int(expression[ind+1]))] + expression[ind+2:]
	return new_expression

def evaluate_no_parens(expression):
	expression = expression.split(" ")
	while '+' in expression:
		expression = remove_one(expression, '+')
	while '*' in expression:
		expression = remove_one(expression, '*')
	return expression[0]


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