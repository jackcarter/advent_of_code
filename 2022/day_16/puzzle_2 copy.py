import re
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict
import time
import functools, itertools

start_time = time.perf_counter()

with open("data.txt") as data:
	lines = data.read().splitlines()

valves = {}
for line in lines:
	valve, flow, tunnels = re.findall(r'Valve ([A-Z][A-Z]) has flow rate=(-?\d+); tunnels? leads? to valves? (.*)', line)[0]
	flow = int(flow)
	tunnels = set(tunnels.split(', '))
	valves[valve] = (flow, tunnels)
#print(valves)

G = nx.Graph()
for valve, (flow, tunnels) in valves.items():
	for tunnel in tunnels:
		G.add_node(tunnel, flow=flow)
		G.add_edge(valve, tunnel)

@functools.lru_cache(maxsize=None)
def path_to_valve(current, target):
	if target is None:
		return [current]*100
	return nx.shortest_path(G, current, target)

def flow_per_step(open_valves):
	return sum(valves[v][0] for v in open_valves)

max_steps = 26

nonzero_valves = tuple([v for v in valves if valves[v][0] != 0])
current = 'AA'
elephant_current = 'AA'

startnodes = ['AA']
startnodes.extend(nonzero_valves)
endnodes = nonzero_valves
print(len(nonzero_valves))
nodecosts = {startnode: {endnode: len(path_to_valve(startnode,endnode)) for endnode in endnodes} for startnode in startnodes}

# generate all routes with cost less than max_steps
routes = []
