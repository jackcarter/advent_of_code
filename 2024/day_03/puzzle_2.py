import re

with open("./data.txt") as data:
	lines = ''.join(data.readlines())

x = re.findall(r'do\(\)|don\'t\(\)|mul\(\d{1,3},\d{1,3}\)', lines)
doing = True
cumsum = 0
for command in x:
	if command == "do()":
		doing = True
	elif command == "don't()":
		doing = False
	else:
		if doing:
			a, b = re.findall(r'\d{1,3}', command)
			cumsum += int(a)*int(b)
print(cumsum)