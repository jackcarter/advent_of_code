def count_distinct(abc):
	return len(dict.fromkeys(abc))

groups = []
with open("data.txt") as data:
	lines = data.read().splitlines()
lines.append('') #ensure we 'flush' the last group to groups list

accumulator = []
for line in lines:
	if line != '':
		accumulator.append(line)
	else:
		groups.append(''.join(accumulator))
		accumulator = []

sum_answers = 0
for group in groups:
	sum_answers += count_distinct(group)

print(sum_answers)

# Answer: 6521