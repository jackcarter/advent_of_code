import re

with open("data.txt") as data:
	lines = data.read().splitlines()

def len_inmem(string):
	string2 = string[1:-1] # remove outside quotes
	string2 = re.sub(r'\\"', '"', string2) # remove escaped quotes
	string2 = re.sub(r'\\\\', '$', string2) # remove double-backslash
	string2 = re.sub(r'\\x..', '$', string2) # remove hex
	return len(string2)

count_literal = 0
count_inmem = 0

for line in lines:
	l1 = len(line)
	l2 = len_inmem(line)
	count_literal += l1 
	count_inmem += l2

print(count_literal - count_inmem)

# Answer: 1342