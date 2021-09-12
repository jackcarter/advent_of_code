import networkx as nx

with open("data.txt") as data:
	lines = data.read().splitlines()

G = nx.Graph()

for line in lines:
	l, r = line.split(' = ')
	c1, c2 = l.split(' to ')
	G.add_edge(c1, c2, weight = int(r))

sp = dict(nx.all_pairs_shortest_path(G))

shortest_path = nx.algorithms.approximation.traveling_salesman.traveling_salesman_problem(G, cycle=False, method=nx.algorithms.approximation.traveling_salesman.greedy_tsp)

total_length = 0
for ii in range(len(shortest_path)-1):
	run_length = G[shortest_path[ii]][shortest_path[ii+1]]['weight']
	total_length += run_length

print(total_length)

# Answer: 117