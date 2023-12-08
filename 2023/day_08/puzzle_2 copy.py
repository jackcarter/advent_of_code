import re
from operator import itemgetter
with open("./data.txt") as data:
	lines = data.read().splitlines()

dirs = lines[0]

nodes = {}
for line in lines[2:]:
	parts = line.split(' = ')
	nodes[parts[0]] = parts[1][1:-1].split(', ')

a_starts =[node for node in nodes.keys() if node[-1]=='A']
print(a_starts)

index = 0
while 1:
	for ii, name in enumerate(a_starts):
		l_r = 0 if dirs[index % len(dirs)] == 'L' else 1
		a_starts[ii] = nodes[a_starts[ii]][l_r]
		index += 1
	if all([n[-1] == 'Z' for n in a_starts]):
		break
	if index % 100000 == 0:
		print(index)
print(index)