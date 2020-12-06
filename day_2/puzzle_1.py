def is_valid(line):
	policy, password = line.split(": ")
	rangetxt, letter = policy.split(" ")
	mini, maxi = map(int, rangetxt.split("-"))
	return mini <= password.count(letter) <= maxi

num_valid = 0
with open("data.txt") as data:
	lines = data.readlines()
	for ii, line in enumerate(lines):
		if is_valid(line):
			num_valid += 1
print(num_valid)		
# Answer: 219