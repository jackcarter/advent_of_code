import re

with open("data.txt") as data:
	lines = data.read().splitlines()

wires = {}

for line in lines:
	left, out = line.split(' -> ')
	wires[out] = left

def memoize(f):
	# taken from https://www.python-course.eu/python3_memoization.php
	memo = {}
	def helper(x):
		if x not in memo:            
			memo[x] = f(x)
		return memo[x]
	return helper

@memoize
def get_signal(start_wire):
	if re.match(r'^\d+$', start_wire.strip()):
		signal = start_wire
	else:
		input_str = wires[start_wire]
		if "NOT" in input_str:
			signal = ~ get_signal(input_str.split(' ')[1]) + 2**16
		elif "AND" in input_str:
			signal = get_signal(input_str.split(' ')[0]) & get_signal(input_str.split(' ')[2])
		elif "OR" in input_str:
			signal = get_signal(input_str.split(' ')[0]) | get_signal(input_str.split(' ')[2])
		elif "LSHIFT" in input_str:
			signal = get_signal(input_str.split(' ')[0]) << get_signal(input_str.split(' ')[2])
		elif "RSHIFT" in input_str:
			signal = get_signal(input_str.split(' ')[0]) >> get_signal(input_str.split(' ')[2])
		else:
			signal = get_signal(input_str)
	return int(signal)

print(get_signal('a'))
# Answer: 3176