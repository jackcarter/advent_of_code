import math

with open("./data.txt") as data:
	lines = data.read().splitlines()

equations = []
for line in lines:
	s = line.split(': ')
	equations.append((int(s[0]), list(map(int, s[1].split()))))

def check(output, inputs, operators):
    if len(inputs) == 1:
        return inputs[0] == output
    cumulative = inputs[0]
    for i in range(1, len(inputs)):
        cumulative = operators[i-1]([cumulative, inputs[i]])
    return cumulative == output

def try_make(output, inputs):
	operators = [None]*(len(inputs)-1)
	for i in range(2**len(operators)):
		# try each combination of math.prod and math.sum
		for j in range(len(operators)):
			if i & (1 << j):
				operators[j] = math.fsum
			else:
				operators[j] = math.prod
		if check(output, inputs, operators):
			return True
	return False
	
cumsum = 0
for output, inputs in equations:
	if try_make(output, inputs):
		cumsum += output
print(cumsum)