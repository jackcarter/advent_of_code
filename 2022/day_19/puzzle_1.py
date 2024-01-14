import time
start_time = time.perf_counter()

import re, math

with open("data.txt") as data:
	lines = data.read().splitlines()

def get_options(state, blueprint, max_minutes):
	robots, materials, minute = state
	# options will be a list of new state tuples (new_robots, new_materials, new_minute)
	# it will represent all meaningful "next states" from the current state
	options = []
	number_materials = len(materials)
	for i, costs in enumerate(blueprint):
		# if we can afford to build a robot, build it
		if all([materials[j] >= costs[j] for j in range(number_materials)]):
			new_robots = list(robots).copy()
			new_robots[i] += 1
			new_materials = tuple([x[0] - x[1] for x in zip(materials, costs)])
			if minute + 1 > max_minutes:
				continue
			options.append((new_robots, new_materials, minute + 1))
		# if we can't afford to build a robot, but we have enough robots producing materials to build one in the future, wait
		elif all([robots[j] > 0 or costs[j] == 0 for j in range(number_materials)]):
			wait_times = [0]*number_materials
			for k in range(number_materials):
				if costs[k] > 0:
					wait_times[k] = math.ceil((costs[k] - materials[k]) / robots[k])
			wait_time = max(wait_times)
			if wait_time + minute > max_minutes:
				continue
			new_robots = list(robots).copy()
			new_robots[i] += 1 # buy the robot we're evaluating
			new_materials = tuple([x[0] + x[1]*wait_time - x[2] for x in zip(materials, robots, costs)])
			if any([x < 0 for x in new_materials]):
				print("error")
				print(new_materials)
				print(materials)
				print(robots)
				print(costs)
				print(wait_time)
				input()
			options.append((new_robots, new_materials, minute + wait_time))
	return options

def prune(frontier, blueprint):
	new_frontier = []
	for i, state in enumerate(frontier):
		robots, materials, minute = state
		# remove all states where (robots producing material X) > (max amount of material X required for building any robot)
		if all([robots[i] > max([x[i] for x in blueprint]) for i in range(3)]):
			continue

		new_frontier.append(state)
	print("pruned:")
	print(len(frontier) - len(new_frontier))
	if len(frontier) - len(new_frontier) > 0:
		input()

	return new_frontier
		

def bfs(blueprint):
	max_minutes = 24
	robots = (1, 0, 0, 0) # ore, clay, obsidian, geode
	materials = (0, 0, 0, 0) # ore, clay, obsidian, geode
	minute = 0
	state = (robots, materials, minute)
	frontier = [state]
	visited = []
	while len(frontier) > 0:
		print(len(frontier), len(visited), len(frontier)/len(visited) if len(visited) > 0 else 0)
		state = frontier.pop()
		
		options = get_options(state, blueprint, max_minutes)
		print("options:", options)
		print("state:", state)
		#input()
		for i, option in enumerate(options):
			if option not in visited:
				frontier.append(option)
				visited.append(option)
		#frontier = prune(frontier, blueprint)
	return max([x[0][3] for x in visited])

blueprints = []
for line in lines:
	data = re.findall(r'Blueprint \d+: Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.', line)[0]
	ore_robot = (int(data[0]), 0, 0, 0)
	clay_robot = (int(data[1]), 0, 0, 0)
	obsidian_robot = (int(data[2]), int(data[3]), 0, 0)
	geode_robot = (int(data[4]), 0, int(data[5]), 0)
	blueprints.append((ore_robot, clay_robot, obsidian_robot, geode_robot))
print("blueprints")
print(blueprints)

print(bfs(blueprints[0]))

print(time.perf_counter() - start_time)