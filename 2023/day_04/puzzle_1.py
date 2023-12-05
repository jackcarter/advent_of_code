with open("./data.txt") as data:
	lines = data.readlines()

def parse_line(line):
	line = line.replace('  ', ' ')
	line = line.replace('\n', '')
	trimmed = line.split(': ')[1]
	winners = trimmed.split(' | ')[0].split(' ')
	numbers = trimmed.split(' | ')[1].split(' ')
	return winners, numbers

sum = 0
for line in lines:
	matches = 0
	winners, numbers = parse_line(line)
	matches = [n for n in numbers if n in winners]
	if matches:
		sum += 2**(len(matches)-1)
print(sum)