import numpy as np
with open("data.txt") as data:
	lines = data.read().splitlines()

registers = [1]

for line in lines:
	if 'noop' in line:
		registers.append(registers[-1])
	elif 'add' in line:
		registers.append(registers[-1]) #wait one cycle
		registers.append(registers[-1] + int(line.split()[1]))

for r in range(6):
	for c in range(40):
		reg = registers[r*40 + c]
		if reg in [c-1, c, c+1]:
			print('#', end='')
		else:
			print('.', end='')
	print()
