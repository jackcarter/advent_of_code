def parse_line(line):
	return line[0], int(line[1:])

def add(a, b):
	return a+b

def subtract(a, b):
	return a-b

def turn(direction, degrees):
	if degrees==180:
		state["wayy"] *= -1
		state["wayx"] *= -1
	elif (degrees == 90 and direction == "L") or (degrees == 270 and direction == "R"):
		new_wayy = state["wayx"]
		new_wayx = -state["wayy"]
		state["wayy"] = new_wayy
		state["wayx"] = new_wayx
	else:
		new_wayy = -1*state["wayx"]
		new_wayx = state["wayy"]
		state["wayy"] = new_wayy
		state["wayx"] = new_wayx


dirmap = {"N": ("wayy", add), "S": ("wayy", subtract), "E": ("wayx", add), "W": ("wayx", subtract)}
frmap = {"F": add, "R": subtract}

def go(line):
	action, num = parse_line(line)
	if action in "NEWS":
		coord, func = dirmap[action]
		state[coord]=func(state[coord], num)
	elif action in "RL":
		turn(action, num)
	elif action == "F":
		for ii in range(num):
			state["x"] += state["wayx"]
			state["y"] += state["wayy"]
	print(action, num, state)

with open("data.txt") as data:
	lines = data.read().splitlines()

state = {"dir": "E", "x": 0, "y": 0, "wayx": 10, "wayy": 1}

for line in lines:
	go(line)

print(abs(state['x'])+abs(state['y']))

# Answer: 45763