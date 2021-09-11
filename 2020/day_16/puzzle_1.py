import itertools
from pprint import pprint

def parse_rules(line):
	field, rules = line.split(": ")
	r1, r2 = rules.split(" or ")
	r1min, r1max = list(map(int, r1.split("-")))
	r2min, r2max = list(map(int, r2.split("-")))
	#return field, lambda x: r1min <= x <= r1max or r2min <= x <= r2max
	return lambda x: r1min <= x <= r1max or r2min <= x <= r2max

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
				func = parse_rules(line)
				rules[ii] = func
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
			invalid_tickets.append(f)
print(sum(invalid_tickets))

# Answer: 22977