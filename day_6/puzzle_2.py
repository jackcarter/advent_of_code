def count_agreement(group_answers):
	setlist = []
	for ga in group_answers:
		setlist.append(set(ga))

	return len(set.intersection(*setlist))

groups = []
with open("data.txt") as data:
	lines = data.read().splitlines()
lines.append('') #ensure we 'flush' the last group to groups list

accumulator = []
for line in lines:
	if line != '':
		accumulator.append(line)
	else:
		groups.append(accumulator)
		accumulator = []

sum_answers = 0
for group in groups:
	sum_answers += count_agreement(group)

print(sum_answers)

# Answer: 3305