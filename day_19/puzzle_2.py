import itertools
from pprint import pprint
import numpy as np
from copy import deepcopy
import operator
import re

def evaluate_rule(rules, rule):
	rule_regex = ""
	if '"' in rule:
		return rule[1] 
	elif "|" in rule:
		rule_parts = rule.split(" | ")
		sub_evals =[evaluate_rule(rules, rp) for rp in rule_parts] 
		return "((" + ")|(".join(sub_evals) + "))"
	else:
		sub_rules = rule.split(" ")
		sub_evals = [evaluate_rule(rules, rules[sr]) for sr in sub_rules]
		if rule == "42 31":
			recursion_limit = 10
			sub_rule = "("
			for ii in range(1,recursion_limit):
				#I don't want to do recursive groups. Assume that there won't be more than 10 levels of recursion...
				sub_rule += f"(({sub_evals[0]}){{{ii}}}({sub_evals[1]}){{{ii}}})" 
				if ii < recursion_limit - 1:
					sub_rule += "|"
			sub_rule += ")"
		else:
			sub_rule = "(" + "".join([item for sublist in sub_evals for item in sublist]) + ")"
		if rule == "42":
			sub_rule = "(" + sub_rule + "+)"
		return sub_rule


with open("data.txt") as data:
	lines = data.read().splitlines()

rules = {}
messages = []
section = 0
for line in lines:
	if line == "":
		section += 1
		continue
	if section == 0:
		rulenum, rule = line.split(": ")
		rules[rulenum] = rule
	elif section == 1:
		messages.append(line)

rule0 = evaluate_rule(rules, rules["0"])
pattern = re.compile('^' + rule0 + '$')
print("Answer:",len([1 for message in messages if pattern.match(message)]))

# Answer: 296