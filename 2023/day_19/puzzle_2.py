from copy import deepcopy
import math
with open("./data.txt") as data:
	lines = data.read().split('\n\n')
	instructionlines = lines[0].splitlines()
	partlines = lines[1].splitlines()

workflows = {}
for il in instructionlines:
	iname, il = il.split('{')
	il = il[:-1]
	itxt = il.split(',')
	workflows[iname] = itxt

parts = []
for pl in partlines:
	part = {}
	ptxt = pl[1:-1].split(',')
	for p in ptxt:
		k, v = p.split('=')
		part[k] = v
	parts.append(part)

def apply_workflow(part):
	active_workflow = 'in'
	_ = 0
	while True:
		_+=1
		if active_workflow == 'A':
			return True
		elif active_workflow == 'R':
			return False
		for instruction in workflows[active_workflow]:
			if instruction == 'A':
				return True
			elif instruction == 'R':
				return False
			else:
				if ':' in instruction:
					a, b = instruction.split(':')[0], instruction.split(':')[1]
					if '<' in a:
						k, r = a.split('<')[0], a.split('<')[1]
						if int(part[k]) < int(r):
							active_workflow = b
							break
						else:
							continue
					elif '>' in a:
						k, r = a.split('>')[0], a.split('>')[1]
						if int(part[k]) > int(r):
							active_workflow = b
							break
						else:
							continue
				else:
					active_workflow = instruction
	
def total_rating(part):
	rating = 0
	for k, v in part.items():
		rating += int(v)
	return rating

def empty_valid_range():
	return {'x': [], 'm': [], 'a': [], 's': []}

def process_instruction(instruction, valid_ranges):
	print("pi", instruction, valid_ranges)
	if instruction == 'A':
		return valid_ranges
	elif instruction == 'R':
		return empty_valid_range()
	else:
		if ':' in instruction:
			a, next_workflow = instruction.split(':')[0], instruction.split(':')[1]
			if '<' in a:
				attribute, criterion = a.split('<')[0], a.split('<')[1]
				print("vra, a", valid_ranges, attribute)
				for ii in range(len(valid_ranges[attribute])):
					if int(criterion) in range(valid_ranges[attribute][ii][0], valid_ranges[attribute][ii][1]):
						print("aiv", attribute, ii, valid_ranges[attribute])
						apply_range = (valid_ranges[attribute][ii][0], int(criterion))
						untouched_range = (int(criterion)+1, valid_ranges[attribute][ii][1])
						valid_ranges[attribute].pop(ii)
						new_valid_ranges = deepcopy(valid_ranges)
						new_valid_ranges[attribute].append(apply_range)
						print(apply_range, untouched_range)
						new_valid_ranges = process_workflow(next_workflow, new_valid_ranges)
						return new_valid_ranges
			elif '>' in a:
				attribute, criterion = a.split('>')[0], a.split('>')[1]
				for ii in range(len(valid_ranges[attribute])):
					if int(criterion) in range(valid_ranges[attribute][ii][0], valid_ranges[attribute][ii][1]):
						untouched_range = (valid_ranges[attribute][ii][0], int(criterion))
						apply_range = (int(criterion)+1, valid_ranges[attribute][ii][1])
						valid_ranges[attribute].pop(ii)
						new_valid_ranges = deepcopy(valid_ranges)
						new_valid_ranges[attribute].append(apply_range)
						print(apply_range, untouched_range)
						new_valid_ranges = process_workflow(next_workflow, new_valid_ranges)
						return new_valid_ranges
		else:
			next_workflow = instruction
			return process_workflow(next_workflow, valid_ranges)

def process_workflow(workflow_id, valid_ranges):
	if workflow_id == 'A':
		return valid_ranges
	elif workflow_id == 'R':
		return empty_valid_range()
	print(workflow_id, valid_ranges)
	input("next")
	workflow = workflows[workflow_id]
	for instruction in workflow:
		valid_ranges = process_instruction(instruction, valid_ranges)
	return valid_ranges

def count_ratings(valid_ranges):
	active_workflow = 'in'
	valid_ranges = process_workflow(active_workflow, valid_ranges)
	return math.prod([int(v) for k, v in valid_ranges.items()])

combinations = count_ratings({'x': [(1,4000)], 'm': [(1,4000)], 'a': [(1,4000)], 's': [(1,4000)], })

print(combinations)