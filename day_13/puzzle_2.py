import itertools

with open("data.txt") as data:
	lines = data.read().splitlines()

buses = [[ii, int(t)] for ii, t in enumerate(lines[1].split(",")) if t != 'x']
print(buses)

time = 0
step = 1
for bus in buses:
    while True:
        time += step
        if (time + bus[0]) % bus[1] == 0:
            break
    step *= bus[1]
    print(bus[1], step)
print(time)

# Answer: 538703333547789