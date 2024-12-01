with open("./data.txt") as data:
	lines = data.readlines()
	left = []
	right = {}
	for i, line in enumerate(lines):
		ab = line.split('   ')
		left.append(int(ab[0]))
		if int(ab[1]) in right:
			right[int(ab[1])] += 1
		else:
			right[int(ab[1])] = 1
	sum = 0
	for n in left:
		if n in right:
			print(n, right[n])
			sum += n*right[n]
	print(sum)