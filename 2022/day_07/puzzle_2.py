with open("data.txt") as data:
	lines = data.read().splitlines()

def flush(ls_output):
	if ls_output:
		for i in ls_output:
			if i[0:3] == 'dir':
				dirname = current + '/' + i.split(' ')[-1]
				parents[dirname] = current
				sizes[dirname] = 0
			else:
				size, _ = i.split(' ')
				size = int(size)
				#parents[(size, name)] = current
				sizes[current] += size
				t = current
				while parents[t] != None:
					t = parents[t]
					sizes[t] += size

ls_output = []
current = 'root'
parents = {'root': None}
sizes = {'root' : 0}
for i, line in enumerate(lines[1:]):
	if line[0] != '$':
		ls_output.append(line)
	else:
		if ls_output:
			flush(ls_output)
			ls_output = []
		if '$ cd' in line:
			if '..' in line:
				current = parents[current]
			else:
				current = current + '/' + line[5:]
flush(ls_output)

unused_needed = 70000000 - 30000000
excess = int(sizes['root']) - unused_needed
print(min([int(s) for (d, s) in sizes.items() if int(s) > excess]))