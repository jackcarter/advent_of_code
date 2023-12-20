from copy import deepcopy
import math
with open("./data.txt") as data:
	lines = data.read().split('\n\n')
	instructionlines = lines[0].splitlines()

workflows = {}
for il in instructionlines:
	iname, il = il.split('{')
	il = il[:-1]
	itxt = il.split(',')
	workflows[iname] = itxt

def next_steps(outcome, workflow_id, ranges):
	next_steps = []
	if workflow_id in ['A', 'R']:
		outcome = workflow_id
		next_steps.append((outcome, None, ranges))
	elif workflow_id is None:
		next_steps.append((outcome, None, ranges))
	else:
		for instruction in workflows[workflow_id]:
			if instruction in ['A', 'R']:
				outcome = instruction
				next_steps.append((outcome, None, ranges))
			else:
				if ':' in instruction:
					new_ranges = deepcopy(ranges)
					conditional, next_workflow = instruction.split(':')[0], instruction.split(':')[1]
					if '<' in conditional:
						attribute, newmax = conditional.split('<')[0], conditional.split('<')[1]
						if ranges[attribute][1] < int(newmax):
							# whole range is included. send to next_workflow unchanged.
							# subtract whole range from existing ranges for next instruction
							next_steps.append((None, next_workflow, new_ranges))
							ranges[attribute][0] = int(newmax)
							continue
						elif ranges[attribute][0] < int(newmax):
							# partial range included. split off a new_ranges and send to next_workflow.
							# subtract that sub-range from existing ranges, and send existing ranges to next instruction in this workflow
							new_ranges[attribute][1] = int(newmax) - 1
							next_steps.append((None, next_workflow, new_ranges))

							ranges[attribute][0] = int(newmax)
							continue
						else:
							# no range included. send existing ranges to next instruction in this workflow
							continue
					elif '>' in conditional:
						attribute, newmin = conditional.split('>')[0], conditional.split('>')[1]
						if ranges[attribute][0] > int(newmin):
							# whole range is included. send to next_workflow unchanged.
							# subtract whole range from existing ranges for next instruction
							next_steps.append(None, next_workflow, new_ranges)
							ranges[attribute][1] = int(newmin)
							continue
						elif ranges[attribute][1] > int(newmin):
							# partial range included. split off a new_ranges and send to next_workflow.
							# subtract that sub-range from existing ranges, and send existing ranges to next instruction in this workflow
							new_ranges[attribute][0] = int(newmin) + 1
							next_steps.append((None, next_workflow, new_ranges))
							ranges[attribute][1] = int(newmin)
							continue
						else:
							# no range included. send existing ranges to next instruction in this workflow
							continue
				else:
					next_workflow = instruction
					next_steps.append((None, next_workflow, ranges))
	return next_steps

ranges = {'x': [1,4000], 'm': [1,4000], 'a': [1,4000], 's': [1,4000], }
workflow_id = 'in'
queue = [(None, workflow_id, ranges)]
complete = []
while len(queue) > 0:
	a = queue.pop()
	outcome, workflow_id, ranges = a
	x = next_steps(outcome, workflow_id, ranges)
	for n in x:
		if n[0] is None:
			queue.append(n)
		else:
			complete.append(n)

subtotals = []
for outcome, _, ranges in complete:
	if outcome == 'A':
		subtotals.append(math.prod([max(ranges[k][1] - ranges[k][0] + 1,0) for k in ranges]))
print(sum(subtotals))