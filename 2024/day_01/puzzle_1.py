with open("./data.txt") as data:
	lines = data.readlines()
	left = []
	right = []
	for i, line in enumerate(lines):
		ab = line.split('   ')
		left.append(int(ab[0]))
		right.append(int(ab[1]))
	left.sort()
	right.sort()
	sum = 0
	for i in range(len(left)):
		sum += abs(left[i] - right[i])
	print(sum)