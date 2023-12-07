import re

with open("data.txt") as data:
	lines = data.read().splitlines()

updates = []
for line in lines:
	if '=>' in line:
		updates.append(line.split(' => '))
	else:
		molecule = line

molecules = set()
for update in updates:
	for m in re.finditer(update[0], molecule):
		molecules.add(molecule[:m.start()] + update[1] + molecule[m.end():])

print(len(molecules))