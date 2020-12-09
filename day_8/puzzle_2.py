def parse_line(line):
	ins, num = line.split(" ")
	num = int(num)
	return ins, num

groups = []
with open("data.txt") as data:
	lines = data.read().splitlines()

def get_instructions():
	instructions = {}
	for ii, line in enumerate(lines):
		ins, num = parse_line(line)
		instructions[ii] = {"ins": ins, "num": num, "vis": False}
	return instructions

instructions = get_instructions()
for ii in range(len(instructions)):
	instructions = get_instructions()
	if instructions[ii]['ins'] == 'jmp':
		instructions[ii]['ins'] = 'nop'
	elif instructions[ii]['ins'] == 'nop':
		instructions[ii]['ins'] = 'jmp'
	else:
		continue # no change required to test for this step
	try:
		accumulator = 0
		step = 0
		while True:
			if step==len(instructions):
				break #done
			if instructions[step]['vis'] == True:
				raise Exception
			if instructions[step]['ins'] == "acc": 
				accumulator += instructions[step]['num']
				instructions[step]['vis'] = True
				step += 1
			elif instructions[step]['ins'] == "jmp": 
				instructions[step]['vis'] = True
				step += instructions[step]['num']
			else:
				instructions[step]['vis'] = True
				step += 1
	except Exception:
		continue
	print("Answer:",accumulator)
	break

# Answer: 1976