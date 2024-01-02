import math
import numpy as np
with open("data.txt") as data:
	linegroups = data.read().split('\n\n')

monkeys = {}

for lg in linegroups:
	for line in lg.split('\n'):
		if 'Monkey' in line:
			monkey = line.split(' ')[1][0]
			monkeys[monkey] = {}
		elif 'items' in line:
			items = [int(i) for i in line.split(': ')[1].split(', ')]
		elif 'Operation' in line:
			optxt = line.split(': ')[1].split(' ')
			opfunc = math.prod if optxt[3] == '*' else sum
			opnum = optxt[4]
		elif 'Test' in line:
			test = int(line.split('divisible by ')[1])
		elif 'If true' in line:
			iftrue = line.split('to monkey ')[1]
		elif 'If false' in line:
			iffalse = line.split('to monkey ')[1]
	monkeys[monkey]['items'] = items
	monkeys[monkey]['opfunc'] = opfunc
	monkeys[monkey]['opnum'] = opnum
	monkeys[monkey]['test'] = test
	monkeys[monkey]['iftrue'] = iftrue
	monkeys[monkey]['iffalse'] = iffalse
	monkeys[monkey]['inspectioncount'] = 0

def round(monkeys):
	for _, m in monkeys.items():
		for item in m['items']:
			if m['opnum'] == 'old':
				opnum = item
			else:
				opnum = int(m['opnum'])
			newitem = m['opfunc']([item, opnum])
			newitem = newitem // 3
			next_monkey = m['iftrue'] if newitem % m['test'] == 0 else m['iffalse']
			monkeys[next_monkey]['items'].append(newitem)
			m['inspectioncount'] += 1
		m['items'] = []
	return monkeys

for _ in range(20):
	monkeys = round(monkeys)

ics = [m['inspectioncount'] for _, m in monkeys.items()]

print(math.prod(sorted(ics, reverse=True)[:2]))

