with open("data.txt") as data:
	lines = data.read().splitlines()

total = 0
for line in lines:
	a, b = line.split(',')
	a1, a2 = [int(i) for i in a.split('-')]
	b1, b2 = [int(i) for i in b.split('-')]
	if (a1 <= b1 and a2 >= b2) or (a1 >= b1 and a2 <= b2):
		total += 1
		
print(total)