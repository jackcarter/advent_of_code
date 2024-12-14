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
for step in range(100):
	for robot in robots:
		robot['px'] = (robot['px'] + robot['vx']) % 101
		robot['py'] = (robot['py'] + robot['vy']) % 103

# calculate number of robots in each quadrant


q1 = 0
q2 = 0
q3 = 0
q4 = 0
for robot in robots:
	if robot['px'] < 50 and robot['py'] < 51:
		q1 += 1
	elif robot['px'] > 50 and robot['py'] < 51:
		q2 += 1
	elif robot['px'] < 50 and robot['py'] > 51:
		q3 += 1
	elif robot['px'] > 50 and robot['py'] > 51:
		q4 += 1

print(q1*q2*q3*q4)