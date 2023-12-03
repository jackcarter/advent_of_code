from itertools import product

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

def check_pn_validity(pn):
	candidate_rows = [pn['index'][0]-1, pn['index'][0], pn['index'][0]+1]
	candidate_cols = range(pn['index'][1]-1, pn['index'][1] + len(pn['number'])+1)
	candidate_indices = list(product(candidate_rows, candidate_cols))
	for ci in candidate_indices:
		if ci in symbols:
			return True
	return False

print(sum([int(pn['number']) for pn in part_numbers if check_pn_validity(pn)]))
