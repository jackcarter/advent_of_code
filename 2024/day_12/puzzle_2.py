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

def in_region(node, region):
    if node[0] < 0 or node[0] >= len(lines) or node[1] < 0 or node[1] >= len(lines[0]):
        return False
    return node in region

def get_region_sides(region):
    # number of corners is the same as the number of sides
    corner_count = 0
    node_corner_directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for node in region:
        for node_corner_direction in node_corner_directions:
            # get the adjacent nodes to either side of the corner, plus the corner itself
            nodes_adjacent_to_corner = [(node[0] + node_corner_direction[0], node[1]), (node[0], node[1] + node_corner_direction[1])]
            node_corner = (node[0] + node_corner_direction[0], node[1] + node_corner_direction[1])
            if all([in_region(n, region) for n in nodes_adjacent_to_corner]) and not in_region(node_corner, region):
                # internal corner of region
                corner_count += 1
            if all([not in_region(n, region) for n in nodes_adjacent_to_corner]):
                # external corner of region
                corner_count += 1
    return corner_count


regions = get_all_regions()

total_score = 0
for region in regions:
    sides = get_region_sides(region)
    area = len(region)
    score = sides * area
    total_score += score
print(total_score)