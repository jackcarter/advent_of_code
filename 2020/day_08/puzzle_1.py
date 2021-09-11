def parse_line(line):
	ins, num = line.split(" ")
	num = int(num)
	return ins, num

groups = []
with open("data.txt") as data:
	lines = data.read().splitlines()

instructions = {}
for ii, line in enumerate(lines):
	ins, num = parse_line(line)
	instructions[ii] = {"ins": ins, "num": num, "vis": False}

accumulator = 0
step = 0
while True:
	if instructions[step]['vis'] == True:
		print(accumulator)
		break
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


# Answer: 1709