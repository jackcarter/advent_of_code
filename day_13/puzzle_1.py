import itertools

with open("data.txt") as data:
	lines = data.read().splitlines()

mytime= int(lines[0])

buses = [[ii, int(t)] for ii, t in enumerate(lines[1].split(",")) if t != 'x']
print(buses)

minwait = 999999999999999
for bus in buses:
	waittime = mytime - (mytime%bus[1]) + bus[1]
	if waittime < minwait:
		bestbus = bus
		minwait = waittime
print(bestbus[1]*(minwait-mytime))

# Answer: 5257