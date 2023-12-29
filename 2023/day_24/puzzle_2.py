import z3

with open("./data.txt") as data:
	lines = data.read().splitlines()
     
hails = []
for line in lines:
	pos, vel = line.split(' @ ')
	x, y, z = pos.split(', ')
	vx, vy, vz = vel.split(', ')
	hails.append([[int(x), int(y), int(z)], [int(vx), int(vy), int(vz)]])

rock_pos = z3.RealVector('r', 3)
rock_vel = z3.RealVector('rv', 3)
collision_times = z3.RealVector('c', len(hails))

s = z3.Solver()

for i in range(len(hails)):
	hail_pos, hail_vel = hails[i]
	s.add(rock_pos[0] + rock_vel[0] * collision_times[i] == hail_pos[0] + hail_vel[0] * collision_times[i])
	s.add(rock_pos[1] + rock_vel[1] * collision_times[i] == hail_pos[1] + hail_vel[1] * collision_times[i])
	s.add(rock_pos[2] + rock_vel[2] * collision_times[i] == hail_pos[2] + hail_vel[2] * collision_times[i])

s.check()

print(s.model().eval(sum(rock_pos)))