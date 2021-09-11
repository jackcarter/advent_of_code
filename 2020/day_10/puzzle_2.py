from functools import reduce
import operator

def get_valid_previous(curr_voltage, voltages):
	return [v for v in voltages if 0 < curr_voltage-v < 4]

with open("data.txt") as data:
	lines = list(map(int, data.read().splitlines()))

start = 0
end = max(lines)+3

voltages = [start]
voltages.extend(sorted(lines))
voltages.extend([end])

valid_ways = {0: {"previous": [], "num": 1}}

for voltage in voltages[1:]:
	previous = get_valid_previous(voltage, voltages)
	valid_ways[voltage]={"previous":previous, 
						 "num": sum([valid_ways[p]["num"] for p in previous])}
print(valid_ways[max(lines)]["num"])

# Answer: 6908379398144