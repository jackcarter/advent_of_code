with open("./data.txt") as data:
	lines = data.read().splitlines()

seeds = [int(x) for x in lines[0].split(': ')[1].split(" ")]
maps = []
for line in lines:
	if line == '':
		seeds = maps + seeds
		maps = []
		continue
	if ':' in line:
		continue

	destination, start, length = [int(x) for x in line.split(' ')]
	unchanged = []
	for s in seeds:
		if s>=start and s<start+length:
			maps.append(s-start+destination) 
		else:
			unchanged.append(s)
	seeds = unchanged

seeds = maps + seeds

print(min(seeds))