import numpy as np
import itertools

with open("./data.txt") as data:
	lines = data.read().splitlines()

hails = set()
for line in lines:
	pos, vel = line.split(' @ ')
	x, y, z = pos.split(', ')
	vx, vy, vz = vel.split(', ')
	hails.add(((int(x), int(y), int(z)), (int(vx), int(vy), int(vz))))

xymin = 200000000000000
xymax = 400000000000000

count = 0
for h, h2 in itertools.combinations(hails, 2):
	(x, y, z), (vx, vy, vz) = h
	(x2, y2, z2), (vx2, vy2, vz2) = h2
	# x + a*vx = x2 + b*vx2
	# y + a*vy = y2 + b*vy2
	try:
		s = np.linalg.solve([[vx, -vx2], [vy, -vy2]], [x2 - x, y2 - y])
	except np.linalg.LinAlgError:
		continue # parallel
	if s[0] < 0 or s[1] < 0:
		continue # happened in the past
	xint = s[0]*vx + x
	yint = s[0]*vy + y
	if xint >= xymin and xint <= xymax and yint >= xymin and yint <= xymax:
		count += 1
print(count)