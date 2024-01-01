import re
with open("data.txt") as data:
	lines = data.read().split('\n\n')
	cratelines = lines[0].split('\n')
	movelines = lines[1].split('\n')

def get_initial_stacks(cl):
	stacks = []
	indices = re.finditer(r'\d', cl[-1])
	for i in indices:
		stacks.append([])
		for l in reversed(cl[:-1]):
			if l[i.start()] != ' ':
				stacks[-1].append(l[i.start()])
	return stacks

def move(n, s, d):
	for _ in range(int(n)):
		stacks[int(d)-1].append(stacks[int(s)-1].pop())

stacks = get_initial_stacks(cratelines)
for l in movelines:
	n, s, d = l.split(' ')[1], l.split(' ')[3], l.split(' ')[5]
	move(n, s, d)

print(''.join([s[-1] for s in stacks]))