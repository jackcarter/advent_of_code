with open("data.txt") as data:
	lines = data.read().splitlines()

def priority(char):
	if ord(char) >= ord('a'):
		return ord(char) - 96
	else:
		return ord(char) - 38

def score(line):
	a = line[:len(line)//2]
	b = line[len(line)//2:]
	duped = [x for x in a if x in b][0]
	return priority(duped)

print(sum([score(line) for line in lines]))