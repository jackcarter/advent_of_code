from functools import reduce # Valid in Python 2.6+, required in Python 3
import operator

import itertools

line = """
19,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,751,x,29,x,x,x,x,x,x,x,x,x,x,13,x,x,x,x,x,x,x,x,x,23,x,x,x,x,x,x,x,431,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,17
"""

mytime= 1002578

buses = [[ii, int(t)] for ii, t in enumerate(line.split(",")) if t != 'x']
print(buses)

bigN = reduce(operator.mul, [bus[0] for bus in buses[1:]], 1)
print(bigN)

incrementer = buses[0][1]
for ii in itertools.count(1):
	time = ii*incrementer
	syncs = ['_']*len(buses)
	for jj, bus in enumerate(buses):
		if (time+bus[0]) % bus[1] == 0:
			syncs[jj] = 'X'
		else:
			syncs[jj] = ((time+bus[0]) % bus[1])
	print(syncs, ii, syncs.count('X'))
	good=True
	for bus in buses:
		if (time+bus[0]) % bus[1] != 0:
			good = False
			break
	if good:
		print(time, "win")
		exit(0)
	if ii>350000:
		exit(0)

# missamount + abs(bus[1]-incrementer) * x = bus[1]
	
buses=buses[:3]
incrementer = buses[0][1]
count = 1
max_numgood = 1
for ii in itertools.count(1):
	time=incrementer*ii
	numgood = 0
	for bus in buses:
		if (time+bus[0]) % bus[1] == 0:
			numgood+=1
		else:
			break
	if numgood > max_numgood:
		incrementer *= bus[1]
		max_numgood += 1
		print(numgood, incrementer)
	if numgood==len(buses):
		print(time)
		#exit(0)
	if ii>500:
		exit(0)




# 37x = 19y+13

#if (time+buses[bus_in_q][0]) % buses[bus_in_q][1] == 0:
#		print(time,buses[bus_in_q][0]+time, (time+buses[bus_in_q][0])/buses[bus_in_q][1])
#		incrementer *= (time+buses[bus_in_q][0])/buses[bus_in_q][1]
#		print("inc:",incrementer)
#		bus_in_q+=1
#	if bus_in_q > len(buses):
#		break


# Answer: s