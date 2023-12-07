with open("./data.txt") as data:
	lines = data.read().splitlines()

parsed = [int(x) for x in lines[0].split(': ')[1].split(" ")]
ranges = set()
for ii, parsedline in enumerate(parsed):
	if ii % 2 == 1:
		continue
	else:
		ranges.add((parsed[ii], parsed[ii]+parsed[ii+1]-1))

maps = []
for line in lines[2:]:
	if ':' in line:
		maps.append([])
		continue
	if line == '':
		continue
	map = [int(x) for x in line.split(" ")]
	maps[-1].append(map)

def split_range(r, overlap):
	new_ranges = set()
	if r[0] < overlap[0]:
		new_ranges.add((r[0], overlap[0]-1))
	if r[1] > overlap[1]:
		new_ranges.add((overlap[1]+1, r[1]))
	return new_ranges

for map in maps:
	shifted_ranges = set()
	for destination, map_start, map_length in map:
		for r in ranges.copy():
			overlap = (max(r[0], map_start), min(r[1], map_start+map_length-1))
			if overlap[0] <= overlap[1]:
				ranges.remove(r)
				new_ranges = split_range(r, overlap)
				ranges = ranges | new_ranges
				shifted_ranges.add((overlap[0] + destination - map_start, overlap[1] + destination - map_start))
	ranges = ranges | shifted_ranges    

print(min(min(ranges)))