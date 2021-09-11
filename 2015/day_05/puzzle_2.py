import re

with open("data.txt") as data:
	lines = data.read().splitlines()


def is_nice(word):
	pairs = []
	for ii in range(len(word)-1):
		newpair = word[ii]+word[ii+1]
		if newpair in pairs[:-1]: # [:-1] because the most recent pair added would be an overlap
			break
		else:
			pairs.append(newpair)
	else:
		return False

	for ii in range(2,len(word)):
		if word[ii-2] == word[ii]:
			break
	else:
		return False
	return True

count_nice = 0
for ii, line in enumerate(lines):
	if is_nice(line):
		count_nice += 1
print(count_nice)

# Answer: 51