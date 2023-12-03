from itertools import product
from collections import defaultdict

with open("./data.txt") as data:
	lines = data.readlines()
	part_numbers = []
	symbols = []
	number_accum = []
	for ii, line in enumerate(lines):
		for jj, ch in enumerate(line):
			if ch.isdigit():
				if len(number_accum) == 0:
					number_index = (ii,jj)
				number_accum.append(ch)
			else:
				if len(number_accum) > 0:
					part_numbers.append({"index": number_index, "number": ''.join(number_accum)})
				number_accum = []
				if ch == '.':
					pass
				elif ch != '\n':
					symbols.append((ii,jj))

def get_candidate_indices(pn):
	candidate_rows = [pn['index'][0]-1, pn['index'][0], pn['index'][0]+1]
	candidate_cols = range(pn['index'][1]-1, pn['index'][1] + len(pn['number'])+1)
	return list(product(candidate_rows, candidate_cols))

gear_numbers = defaultdict()
for pn in part_numbers:
	cis = get_candidate_indices(pn)
	for ci in cis:
		try:
			if lines[ci[0]][ci[1]] == '*':
				if ci in gear_numbers:
					gear_numbers[ci].append(pn['number'])
				else:
					gear_numbers[ci] = [pn['number']]
		except IndexError:
			pass
print(gear_numbers)

valid_gns = [gear_numbers[key] for key in gear_numbers if len(gear_numbers[key])==2]
print(valid_gns)
print(sum([int(x[0])*int(x[1]) for x in valid_gns]))

#print(sum([int(pn['number']) for pn in part_numbers if check_pn_validity(pn)]))
