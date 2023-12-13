from functools import cache

with open("./data.txt") as data:
	lines = data.read().splitlines()

@cache
def count_possible_springs(s, n):
	total_hashes = sum(n)
	total_chars = len(s)
	total_dots = total_chars - total_hashes
	possibilities = 0
	if len(n) == 1:
		lookahead = n[0]
		for ii in range(total_chars - lookahead + 1):
			if ii > 0 and s[ii-1] == "#":
				break
			elif "." in s[ii:ii+lookahead]:
				continue
			elif "#" in s[ii+lookahead:]:
				continue
			else:
				possibilities += 1
		return possibilities

	lookahead = n[0]
	for ii in range(total_dots - len(n) + 2): # +2 because we need to account for #s on outside
		lookahead_string = s[ii:ii+lookahead]
		if ii > 0 and s[ii-1] == "#":
			break
		elif "." in lookahead_string or s[ii+lookahead] == "#":
			continue
		elif sum(n[1:]) < s[ii+lookahead+1:].count("#"):
			continue
		else:
			possibilities += count_possible_springs(s[ii+lookahead+1:], n[1:])
	return possibilities


def unfold(s,n):
	return ('?'.join([s]*5), ','.join([n]*5))

total = 0
for ii, line in enumerate(lines):
	a = line.split(' ')
	s, n = unfold(a[0], a[1])
	n = tuple([int(x) for x in n.split(',')]) #tuple so we can cache
	total += count_possible_springs(s, n)
	
print(total)