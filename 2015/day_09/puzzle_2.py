import networkx as nx

with open("data.txt") as data:
	lines = data.read().splitlines()

G = nx.Graph()

cities = set()

for line in lines:
	l, r = line.split(' = ')
	c1, c2 = l.split(' to ')
	G.add_edge(c1, c2, weight = int(r))
	cities.add(c1)
	cities.add(c2)

sp = dict(nx.all_pairs_shortest_path(G))

def get_length(G, path):
	total_length = 0
	for ii in range(len(path)-1):
		run_length = G[path[ii]][path[ii+1]]['weight']
		total_length += run_length
	return total_length

longest_path = 0
for city1 in cities:
	for city2 in cities:
		if city1 == city2:
			break
		all_paths = [path for path in nx.all_simple_paths(G, city1, city2)]		
		temp_longest_path = get_length(G, max(all_paths, key=lambda path: get_length(G, path)))
		if temp_longest_path > longest_path:
			longest_path = temp_longest_path

print(longest_path)

# Answer: 909