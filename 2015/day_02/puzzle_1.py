with open("data.txt") as data:
	lines = data.readlines()

def calc_area(l, w, h):
	sorted_sides = sorted([l,w,h])
	smallest_side_area = sorted_sides[0]*sorted_sides[1]
	return 2*l*w + 2*w*h + 2*l*h + smallest_side_area

presents = []
sqft = 0

for ii, line in enumerate(lines):
	dims = line.split('x')
	dims = map(int, dims)
	presents.append(dims)
	sqft += calc_area(*dims)
print(sqft)

# Answer: 1586300