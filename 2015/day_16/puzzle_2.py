import re

with open("data.txt") as data:
	lines = data.read().splitlines()

criteria = {"children": 3,
"cats": 7,
"samoyeds": 2,
"pomeranians": 3,
"akitas": 0,
"vizslas": 0,
"goldfish": 5,
"trees": 3,
"cars": 2,
"perfumes": 1}

for line in lines:
	sue_num = re.findall(r'Sue (\d+):', line)[0]
	items = line[len('Sue : ')+len(sue_num):].split(', ')
	items = [i.split(': ') for i in items]
	sue = True
	for item in items:
		if item[0] in ['cats', 'trees']:
			if criteria[item[0]] >= int(item[1]):
				sue = False
		elif item[0] in ['pomeranians', 'goldfish']:
			if criteria[item[0]] <= int(item[1]):
				sue = False
		elif criteria[item[0]] != int(item[1]):
			sue = False
	if sue == True:
		print(sue_num)
		exit(0)