target = 15690279

with open("data.txt") as data:
	lines = list(map(int, data.read().splitlines()))

for ii in range(len(lines)):
	for jj, line in enumerate(lines):
		total = sum(lines[ii:jj])
		if total == target:
			print(min(lines[ii:jj])+max(lines[ii:jj]))
			exit(0)
		elif total > target:
			break


# Answer: 2174232