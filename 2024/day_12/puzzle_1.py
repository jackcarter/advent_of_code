with open("./data.txt") as data:
	lines = data.read().splitlines()

def get_neighbors(i, j):
	directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
	potential_neighbors = []
	for d in directions:
		potential_neighbor = (i + d[0], j + d[1])	
		potential_neighbors.append(potential_neighbor)
	return potential_neighbors

def get_valid_neighbors(i, j):
	all_neighbors = get_neighbors(i, j)
	valid_neighbors = []
	for neighbor in all_neighbors:
		if neighbor[0] >= 0 and neighbor[0] < len(lines) and neighbor[1] >= 0 and neighbor[1] < len(lines[0]):
			valid_neighbors.append(neighbor)
	return valid_neighbors

def find_region(i, j, processed_nodes):
	region = set()
	region.add((i, j))
	to_test = get_valid_neighbors(i, j)
	while to_test:
		neighbor = to_test.pop()
		if neighbor in processed_nodes:
			continue
		if lines[neighbor[0]][neighbor[1]] == lines[i][j]:
			region.add(neighbor)
			processed_nodes.add(neighbor)
			to_test.extend(get_valid_neighbors(neighbor[0], neighbor[1]))
	return region

def get_all_regions():
	regions = []
	processed_nodes = set()
	for i in range(len(lines)):
		for j in range(len(lines[i])):
				if (i, j) in processed_nodes:
					continue
				regions.append(find_region(i, j, processed_nodes))
	return regions

def get_region_perimeter(region):
	perimeter = 0
	for node in region:
		neighbors = get_neighbors(node[0], node[1])
		for neighbor in neighbors:
			if neighbor not in region:
				perimeter += 1
	return perimeter

regions = get_all_regions()

total_score = 0
for region in regions:
	perimeter = get_region_perimeter(region)
	area = len(region)
	score = perimeter * area
	total_score += score
print(total_score)
	
