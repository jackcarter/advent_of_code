# slope is expressed as (delta_y, delta_x), y increasing downwards and x increasing to the right

def get_next_pos(slope, x1, y1, shape_width):
	y2 = y1 + slope[0]
	x2 = (x1 + slope[1]) % shape_width
	return x2, y2

array = []
with open("data.txt") as data:
	lines = data.read().splitlines()
	for line in lines:
		array.append(line)


shape_width = len(array[0])
shape_height = len(array)
x = 0
y = 0
slope = [1,3]
print(array)

num_trees = 0
while y < shape_height-1:
	x, y = get_next_pos(slope, x, y, shape_width)
	if array[y][x] == "#":
		num_trees += 1

print(num_trees)

# Answer: 156