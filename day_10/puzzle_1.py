def use_all_adapters(adapters):
	deltas = {1:0,2:0,3:0}

	for ii in range(1,len(adapters)):
		delta = adapters[ii]-adapters[ii-1]
		deltas[delta]+=1
	print(deltas, deltas[1]*deltas[3])

with open("data.txt") as data:
	lines = list(map(int, data.read().splitlines()))

start = 0
end = max(lines)+3

adapters = [start]
adapters.extend(sorted(lines))
adapters.extend([end])

use_all_adapters(adapters)

# Answer: 2080