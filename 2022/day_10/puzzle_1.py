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

print(sum([n*registers[n-1] for n in [20, 60, 100, 140, 180, 220]]))