from math import gcd

with open("./data.txt") as data:
	lines = data.read().splitlines()

dirs = lines[0]

nodes = {}
for line in lines[2:]:
	parts = line.split(' = ')
	nodes[parts[0]] = parts[1][1:-1].split(', ')

ghosts =[node for node in nodes.keys() if node[-1]=='A']

index = 0
cycles = [-1]*len(ghosts)
while 1:
	for ii, name in enumerate(ghosts):
		l_r = 0 if dirs[index % len(dirs)] == 'L' else 1
		ghosts[ii] = nodes[ghosts[ii]][l_r]
		if ghosts[ii][-1] == 'Z':
			cycles[ii] = index + 1
	index += 1
	if all([cycle > -1 for cycle in cycles]):
		break

lcm = 1
for i in cycles:
    lcm = lcm*i//gcd(lcm, i)

print(lcm)