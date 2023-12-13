import itertools
with open("./data.txt") as data:
	lines = data.read().splitlines()

def get_possibilities(s, n):
	total_hashes = sum(n)
	total_chars = len(s)
	total_dots = total_chars - total_hashes
	#get all possible strings of length groups_operational that sum to count_operational
	dots_inner = [[0]+ list(x) + [0] for x in itertools.product(range(1,total_dots+1), repeat=len(n)-1)]
	dots_left = [list(x)+[0] for x in itertools.product(range(1,total_dots+1), repeat=len(n))]
	dots_right = [[0]+list(x) for x in itertools.product(range(1,total_dots+1), repeat=len(n))]
	dots_outer = [list(x) for x in itertools.product(range(1,total_dots+1), repeat=len(n)+1)]
	all_dot_groups = [x for x in itertools.chain(dots_inner, dots_left, dots_right, dots_outer) if sum(x) == total_dots]
	valid_candidates = []
	for permutation in all_dot_groups:
		candidate = ''
		for ii, dot_group in enumerate(permutation):
			candidate += '.'*dot_group
			if ii < len(n):
				candidate += '#'*n[ii]
		for ii in range(len(candidate)):
			if candidate[ii] == s[ii] or s[ii] == '?':
				pass
			else:
				
				break
		else:
			valid_candidates.append(candidate)
	return len(valid_candidates)

total = 0
for ii, line in enumerate(lines):
	a = line.split(' ')
	s = a[0]
	n = [int(x) for x in a[1].split(',')]
	a = get_possibilities(s, n)
	total += a
	
print(total)
