with open("data.txt") as data:
	lines = data.readlines()
floor = 0
for ii, char in enumerate(lines[0]):
	if char == '(':
		floor += 1
	elif char == ')':
		floor -= 1
print(floor)
# Answer: 280