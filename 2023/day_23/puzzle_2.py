import networkx as nx

with open("./data.txt") as data:
	lines = data.read().splitlines()

grid = []
for line in lines:
	grid.append([c for c in line])

def invalid_arrow(direction):
	directions = [(1,0), (-1,0), (0,1), (0,-1)]
	arrows = ['v', '^', '>', '<']
	invalid_arrow = arrows[directions.index((-direction[0], -direction[1]))]
	return invalid_arrow

def get_valid_neighbors(pos, direction):
	r, c = pos
	directions = [(1,0), (-1,0), (0,1), (0,-1)]
	neighbors = [((r + d[0], c + d[1]), d) for d in directions if d != (-direction[0], -direction[1])] # don't go backwards
	neighbors = [n for n in neighbors if n[0][0] >= 0 and n[0][0] < len(grid) and n[0][1] >= 0 and n[0][1] < len(grid[0])] # don't go off grid or on forest
	neighbors = [n for n in neighbors if grid[n[0][0]][n[0][1]] != '#'] # don't go into forest
	return set(neighbors)

def advance_to_next_node(current, direction):
	neighbors = get_valid_neighbors(current, direction)
	edge_len = 1
	while len(neighbors) == 1:
		print("e",edge_len)
		edge_len += 1
		current, direction = next(iter(neighbors))
		if grid[current[0]][current[1]] == invalid_arrow(direction):
			pass # do go up a slippery slope
		neighbors = get_valid_neighbors(current, direction)
	return current, direction, edge_len

# walk until there's a branch (more than one neighbor)
# label that a node and add to graph

start = (0, 1)
direction = (1, 0)
goal = (len(grid) - 1, len(grid[0]) - 2)
frontier = [((start[0]+direction[0], start[1]+direction[1]), direction)]
visited = set()
G = nx.DiGraph()
G.add_node(start)
while len(frontier) > 0:
	print(len(frontier))
	branch_node, direction = frontier.pop()
	edge_node = branch_node[0] - direction[0], branch_node[1] - direction[1]
	current, direction, edge_len = advance_to_next_node(branch_node, direction)
	neighbors = get_valid_neighbors(current, direction)
	if len(neighbors) > 1:
		for n in neighbors:
			if n not in visited:
				frontier.append(n)
			visited.add(n)
		G.add_edge(edge_node, current, weight=edge_len)
	elif current == goal:
		# add edge to goal
		G.add_edge(edge_node, current, weight=edge_len)
	else:
		pass # dead end
print("starting all paths")
all_paths = (path for path in nx.all_simple_paths(G, start, goal))
print("all paths done")
max_length = -1
for p in all_paths:
	# this takes a minute or two
	max_length = max(nx.path_weight(G, p, "weight"), max_length)
print(max_length)