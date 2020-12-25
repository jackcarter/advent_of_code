import itertools
from pprint import pprint

def parse_line(line):
	a, b = line.split(" = ")
	a = int(a[4:-1])
	return a, int(b)

def apply_mask(mask, val):
	binval = [x for x in bin(val)[2:].zfill(len(mask))]
	for ii in range(len(mask)):
		if mask[-ii] !="X":
			binval[-ii] = mask[-ii]
	return int("".join(binval), 2)


with open("data.txt") as data:
	lines = data.read().splitlines()

vals = {}
for line in lines:
	if line[:4] == "mask":
		mask = line[7:]
		continue
	mem, val = parse_line(line)
	val = apply_mask(mask, val)
	vals[mem]=val

print("Answer:",sum(vals.values()))

# Answer: 6386593869035