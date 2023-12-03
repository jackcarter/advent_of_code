with open("./data.txt") as data:
	lines = data.readlines()
	sum = 0
	for line in lines:
		digits = ''.join(c for c in line if c.isdigit())
		sum += int(digits[0])*10 + int(digits[-1])
	print(sum)