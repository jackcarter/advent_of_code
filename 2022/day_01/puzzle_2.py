with open("data.txt") as data:
	lines = data.read().split('\n\n')

elves = []
for group in lines:
	elflines = group.split('\n')
	elves.append(sum([int(line)for line in elflines]))

elves.sort()
print(sum(elves[-3:]))