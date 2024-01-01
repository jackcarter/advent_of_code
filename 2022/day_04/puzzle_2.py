with open("data.txt") as data:
	lines = data.read().splitlines()

total = 0
for line in lines:
	a, b = line.split(',')
	a1, a2 = [int(i) for i in a.split('-')]
	b1, b2 = [int(i) for i in b.split('-')]
	if not (a2 < b1) and not (b2 < a1):
		total += 1

print(total)