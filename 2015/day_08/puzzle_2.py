import re

with open("data.txt") as data:
	lines = data.read().splitlines()

def len_inmem(string):
	string2 = string
	string2 = re.sub(r'"', '--', string2) # "escape" quotes
	string2 = re.sub(r'\\', '--', string2) # "escape" backslashes
	string2 = string2 + "--" # add 2 more chars for external quotes
	return len(string2)

count_literal = 0
count_inmem = 0

for line in lines:
	l1 = len(line)
	l2 = len_inmem(line)
	count_literal += l1 
	count_inmem += l2

print(count_inmem - count_literal)

# Answer: 1342