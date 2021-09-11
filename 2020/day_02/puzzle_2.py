def is_valid(line):
	policy, password = line.split(": ")
	positions, letter = policy.split(" ")
	pos1, pos2 = map(int, positions.split("-"))
	return bool(password[pos1-1] == letter) != bool(password[pos2-1] == letter)

num_valid = 0
with open("data.txt") as data:
	lines = data.readlines()
	for ii, line in enumerate(lines):
		if is_valid(line):
			num_valid += 1
print(num_valid)		
# Answer: 593