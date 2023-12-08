import re
from operator import itemgetter
with open("./data.txt") as data:
	lines = data.read().splitlines()

dirs = lines[0]

nodes = {}
for line in lines[2:]:
	parts = line.split(' = ')
	nodes[parts[0]] = parts[1][1:-1].split(', ')

result = 'AAA'
index = 0
while result != 'ZZZ':
	l_r = 0 if dirs[index % len(dirs)] == 'L' else 1
	result = nodes[result][l_r]
	index += 1
print(index)