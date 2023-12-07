import math
with open("./data.txt") as data:
	lines = data.read().splitlines()

times = [int(i) for i in lines[0].split(" ") if i.isdigit()]
distances = [int(i) for i in lines[1].split(" ") if i.isdigit()]

tds = zip(times, distances)
successful_times = []
for td in tds:
	successful_times.append([])
	for t in range(td[0]):
		v = t
		d = (td[0]-t)*v
		if d > td[1]:
			successful_times[-1].append(t)
print(math.prod([len(i) for i in successful_times]))