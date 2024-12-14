with open("./data.txt") as data:
	lines = data.read().splitlines()

robots = []
for line in lines:
	#p=9,5 v=-3,-3
	p = line.split('=')[1].split(' ')[0].split(',')
	px = p[0]
	py = p[1]
	v = line.split('=')[2].split(',')
	vx = v[0]
	vy = v[1]
	robots.append({'px': int(px), 'py': int(py), 'vx': int(vx), 'vy': int(vy)})

def print_grid(robots):
	grid = [[0 for i in range(101)] for j in range(103)]
	for robot in robots:
		grid[robot['py']][robot['px']] += 1
	for row in grid:
		print(''.join([str(c) if c > 0 else ' ' for c in row ])) 

to_skip = 1
skip_from = 0
for step in range(100000):
	for robot in robots:
		robot['px'] = (robot['px'] + robot['vx']) % 101
		robot['py'] = (robot['py'] + robot['vy']) % 103
	print()
	print('step', step)
	print(step, to_skip, skip_from, step-skip_from, step - skip_from == to_skip)
	if step - skip_from == int(to_skip):
		print_grid(robots)
		to_skip = input()
		skip_from = step
	elif step - skip_from < int(to_skip):
		continue
	else:
		skip_from = step
	if not to_skip:
			to_skip = 103

# scan through manually starting from 48 and stopping when you see a tree :\