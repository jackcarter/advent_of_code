with open("data.txt") as data:
	lines = data.read().splitlines()

def priority(char):
	if ord(char) >= ord('a'):
		return ord(char) - 96
	else:
		return ord(char) - 38

def score(lines):
	a, b, c = lines[0], lines[1], lines[2]
	duped = [x for x in a if x in b and x in c][0]
	return priority(duped)

total = 0
for i in range(0, len(lines), 3):
	total += score(lines[i:i+3])

print(total)