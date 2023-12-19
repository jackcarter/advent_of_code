import re
with open("./data.txt") as data:
	lines = data.read().split('\n\n')
	instructionlines = lines[0].splitlines()
	partlines = lines[1].splitlines()

instructions = {}
for il in instructionlines:
	iname, il = il.split('{')
	il = il[:-1]
	itxt = il.split(',')
	instructions[iname] = itxt

parts = []
for pl in partlines:
	part = {}
	ptxt = pl[1:-1].split(',')
	for p in ptxt:
		k, v = p.split('=')
		part[k] = v
	parts.append(part)

def apply_workflow(part):
	active_instruction = 'in'
	_ = 0
	while True:
		_+=1
		if active_instruction == 'A':
			return True
		elif active_instruction == 'R':
			return False
		for i in instructions[active_instruction]:
			if i == 'A':
				return True
			elif i == 'R':
				return False
			else:
				if ':' in i:
					a, b = i.split(':')[0], i.split(':')[1]
					if '<' in a:
						k, r = a.split('<')[0], a.split('<')[1]
						if int(part[k]) < int(r):
							active_instruction = b
							break
						else:
							continue
					elif '>' in a:
						k, r = a.split('>')[0], a.split('>')[1]
						if int(part[k]) > int(r):
							active_instruction = b
							break
						else:
							continue
				else:
					active_instruction = i
	


def total_rating(part):
	rating = 0
	for k, v in part.items():
		rating += int(v)
	return rating

accepted_parts = []
for part in parts:
	if apply_workflow(part):
		accepted_parts.append(part)

print(sum([total_rating(p) for p in accepted_parts]))