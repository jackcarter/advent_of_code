import itertools
from pprint import pprint
from functools import reduce
import operator

def parse_rules(line):
	field, rules = line.split(": ")
	r1, r2 = rules.split(" or ")
	r1min, r1max = list(map(int, r1.split("-")))
	r2min, r2max = list(map(int, r2.split("-")))
	return field, lambda x: r1min <= x <= r1max or r2min <= x <= r2max
	#return lambda x: r1min <= x <= r1max or r2min <= x <= r2max

with open("data.txt") as data:
	lines = data.read().splitlines()

	section = 0
	rules = {}
	other_tickets = {}
	for ii, line in enumerate(lines):
		if section == 0:
			if line == "":
				section += 1
			else:
				field, func = parse_rules(line)
				rules[field] = func
		elif section == 1:
			if line == "":
				section += 1
			elif line == "your ticket:":
				continue
			else:
				my_ticket = list(map(int,line.split(",")))
		elif section == 2:
			if line == "nearby tickets:":
				continue
			else:
				other_tickets[ii] = list(map(int,line.split(",")))

invalid_tickets = []
for ii, t in other_tickets.items():
	for f in t:
		if not any([rules[r](f) for r in rules]):
			invalid_tickets.append(ii)

for it_id in invalid_tickets:
	del other_tickets[it_id]

ticket_fields = {x: [] for x in range(len(rules))}

#figure out which fields are valid for which rules
for tf in ticket_fields:
	for rule in rules:
		if all([rules[rule](t[tf]) for t in other_tickets.values()]):
			ticket_fields[tf].append(rule)

#assign a single rule to each field
tf2 = {}
while len(tf2) < len(ticket_fields):
	for tf in ticket_fields:
		if len(ticket_fields[tf]) == 1:
			rule_to_remove = ticket_fields[tf][0]
			tf2[tf] = rule_to_remove
			for tf in ticket_fields:
				if rule_to_remove in ticket_fields[tf] and len(ticket_fields[tf]) > 1:
					ticket_fields[tf].remove(rule_to_remove)

print("Answer:",reduce(operator.mul, [my_ticket[num] for num, name in tf2.items() if name.startswith('departure')], 1))

# Answer: 998358379943