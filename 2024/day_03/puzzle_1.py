import re

with open("./data.txt") as data:
	lines = ''.join(data.readlines())

x = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', lines)
total = sum([int(a)*int(b) for a, b in x])
print(total)
