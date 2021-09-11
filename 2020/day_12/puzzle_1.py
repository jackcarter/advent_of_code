def parse_line(line):
	return line[0], int(line[1:])

def add(a, b):
	return a+b

def subtract(a, b):
	return a-b

dirmap = {"N": ("y", add), "S": ("y", subtract), "E": ("x", add), "W": ("x", subtract)}
frmap = {"F": add, "R": subtract}

def go(line):
	action, num = parse_line(line)
	if action in "NEWS":
		coord, func = dirmap[action]
		state[coord]=func(state[coord], num)
	elif action == "R":
		state["dir"] = "NESWNESW"["NESW".index(state["dir"])+num//90] #awful!
	elif action == "L":
		state["dir"] = "WSENWSEN"["WSEN".index(state["dir"])+num//90]
	elif action == "F":
		coord, func = dirmap[state["dir"]]
		state[coord] = func(state[coord], num)
	print(action, num, state)

with open("data.txt") as data:
	lines = data.read().splitlines()

state = {"dir": "E", "x": 0, "y": 0}

for line in lines:
	go(line)

print(abs(state['x'])+abs(state['y']))

# Answer: 759