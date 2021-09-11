with open("data.txt") as data:
	lines = data.readlines()

def calc_ribbon(l, w, h):
	sorted_sides = sorted([l,w,h])
	smallest_side_perimeter = 2*sorted_sides[0] + 2*sorted_sides[1]
	return l*w*h + smallest_side_perimeter

presents = []
sqft = 0

for ii, line in enumerate(lines):
	dims = line.split('x')
	dims = map(int, dims)
	presents.append(dims)
	sqft += calc_ribbon(*dims)
print(sqft)

# Answer: 3737498