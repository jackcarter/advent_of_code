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
		return "(" + "".join([item for sublist in sub_evals for item in sublist]) + ")"


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

pattern = re.compile('^' + evaluate_rule(rules, rules["0"]) + '$')

print("Answer:",len([1 for message in messages if pattern.match(message)]))

# Answer: 192