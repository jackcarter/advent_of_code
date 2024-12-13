with open("./data.txt") as data:
	lines = data.read().splitlines()

machines = []
a=None
b=None
prize=None
for line in lines:
	if "Button A: "	in line:
		# parse numbers from "Button A: X+94, Y+34"
		a = [int(i) for i in line.split("Button A: X+")[1].split(", Y+")]
	elif "Button B: " in line:
		b = [int(i) for i in line.split("Button B: X+")[1].split(", Y+")]
	elif "Prize: " in line:
		prize = [int(i) for i in line.split("Prize: X=")[1].split(", Y=")]
		machines.append({'a':a, 'b':b, 'prize':prize})

a_cost = 3
b_cost = 1

total_tokens = 0
machines_won = []
for a_presses in range(100):
	for b_presses in range(100):
		for machine in machines:
			prize = machine['prize']
			a = machine['a']
			b = machine['b']
			if (a_presses * a[0] + b_presses * b[0]) == prize[0] and (a_presses * a[1] + b_presses * b[1]) == prize[1]:
				tokens = a_presses * a_cost + b_presses * b_cost
				total_tokens += tokens
print(total_tokens)