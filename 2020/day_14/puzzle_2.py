import itertools
from pprint import pprint
from copy import deepcopy

def parse_line(line):
	a, b = line.split(" = ")
	a = int(a[4:-1])
	return a, int(b)

def get_floating_mems(binval):
	if len(binval) == 0:
		return []
	mems = [[]]
	for ii in range(len(binval)):
		if binval[ii] != 'X':
			for mem in mems:
				mem.append(binval[ii])
		else:
			newmems1 = [mem + ['1'] for mem in mems]
			newmems0 = [mem + ['0'] for mem in mems]
			mems = newmems1 + newmems0
	return mems

def get_memory_addresses(mask, val):
	binval = [x for x in bin(val)[2:].zfill(len(mask))]
	for ii in range(len(mask)):
		if mask[-ii] =="1":
			binval[-ii] = "1"
		elif mask[-ii] =="X":
			binval[-ii] = "X"
	binvals = get_floating_mems(binval)
	decvals = []
	for b in binvals:
		decvals.append(int("".join(b), 2))
	return decvals

with open("data.txt") as data:
	lines = data.read().splitlines()

vals = {}
for ii, line in enumerate(lines):
	if line[:4] == "mask":
		mask = line[7:]
		continue
	mem, val = parse_line(line)
	mems = get_memory_addresses(mask, mem)
	for mem in mems:
		vals[mem] = val

print("Answer:",sum(vals.values()))

# Answer: 4288986482164