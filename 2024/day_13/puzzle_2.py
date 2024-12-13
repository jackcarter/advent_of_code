from math import gcd

# using https://math.stackexchange.com/questions/20717/how-to-find-solutions-of-linear-diophantine-ax-by-c

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
		prize = [10000000000000+int(i) for i in line.split("Prize: X=")[1].split(", Y=")]
		machines.append({'a':a, 'b':b, 'prize':prize})

a_cost = 3
b_cost = 1

total_cost = 0
for machine in machines:
	px = machine['prize'][0]
	py = machine['prize'][1]
	ax = machine['a'][0]
	ay = machine['a'][1]
	bx = machine['b'][0]
	by = machine['b'][1]
	# solve the system of equations with Cramer's Rule
	a_presses = (px*by - py*bx) / (ax*by - ay*bx)
	b_presses = (ax*py - ay*px) / (ax*by - ay*bx)
	if a_presses != int(a_presses) or b_presses != int(b_presses):
		continue
	total_cost += int(a_presses * a_cost + b_presses * b_cost)

print(total_cost)
