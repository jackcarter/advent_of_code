import re

with open("data.txt") as data:
	lines = data.read().splitlines()

updates = []
for line in lines:
	if '=>' in line:
		updates.append(line.split(' => '))
	else:
		molecule = line

reverse_updates = []
for update in updates:
	reverse_updates.append([update[1], update[0]])

reverse_updates.sort(key=lambda x: len(x[0]), reverse=True)

target = 'e'

count = 0
while molecule != target:
	count+=1
	for update in reverse_updates:
		if update[0] in molecule:
			molecule = molecule.replace(update[0], update[1], 1)
			break

print(count)