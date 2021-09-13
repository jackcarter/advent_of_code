import re

with open("data.txt") as data:
	text = data.read()

numbers = map(int, re.findall(r'-?\d+', text))

print(sum(numbers))

# Answer: 111754