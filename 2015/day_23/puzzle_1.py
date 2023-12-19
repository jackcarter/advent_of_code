from copy import deepcopy
import math

with open("data.txt") as data:
    lines = data.read().splitlines()
instructions = []
for line in lines:
    register = None
    value = None
    if ',' in line:
        instruction, value = line.split(', ')
        instruction, register = instruction.split(' ')
        value = int(value[1:])
    elif '+' in line:
        instruction, value = line.split(' +')
        value = int(value)
    elif 'jmp' in line:
        instruction, value = line.split(' ')
        value = int(value)
    else:
        instruction, register = line.split(' ')
    instructions.append((instruction, register, value))

registers = {'a': 0, 'b': 0}
_ = 0
while _ < len(instructions):
    instruction, register, value = instructions[_]
    if instruction == 'jmp':
        _ += value
        continue
    elif instruction == 'jie':
        if registers[register] % 2 == 0:
            _ += value
            continue
    elif instruction == 'jio':
        if registers[register] == 1:
            _ += value
            continue
    elif instruction == 'inc':
        registers[register] += 1
    elif instruction == 'tpl':
        registers[register] *= 3
    elif instruction == 'hlf':
        registers[register] //= 2
    _ += 1
    
print(registers['b'])

