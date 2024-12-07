import math

with open("./data.txt") as data:
	lines = data.read().splitlines()

equations = []
for line in lines:
	s = line.split(': ')
	equations.append((int(s[0]), list(map(int, s[1].split()))))
 
def concat_op(nums):
	return int(''.join(map(str, nums)))

def check(output, inputs, operators):
    if len(inputs) == 1:
        return inputs[0] == output
    cumulative = inputs[0]
    for i in range(1, len(inputs)):
        cumulative = int(operators[i-1]([cumulative, inputs[i]]))
    return cumulative == output

def try_make(output, inputs):
	operators = [None]*(len(inputs)-1)
	combinations = 3**(len(operators))
	for i in range(combinations):
		temp = i
		for j in range(len(operators)):
				operator_choice = temp % 3
				if operator_choice == 0:
						operators[j] = math.fsum
				elif operator_choice == 1:
						operators[j] = math.prod
				else:
						operators[j] = concat_op
				temp //= 3
		if check(output, inputs, operators):
				return True
	return False
	
cumsum = 0
for i, (output, inputs) in enumerate(equations):
	if i % 100 == 0:
		print(i)
	if try_make(output, inputs):
		cumsum += output
print(cumsum)