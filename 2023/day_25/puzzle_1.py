import networkx as nx
import math

with open("./data.txt") as data:
	lines = data.read().splitlines()

G = nx.Graph()
for line in lines:
	edges = line.split(': ')
	for to_edge in edges[1].split(' '):
		G.add_edge(edges[0], to_edge)

x = nx.minimum_edge_cut(G)
if len(x) != 3:
	print("ERROR")
	exit(0)

G.remove_edges_from(x)

print(math.prod([len(i) for i in nx.connected_components(G)]))