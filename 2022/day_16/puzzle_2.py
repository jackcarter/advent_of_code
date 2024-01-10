import re
import networkx as nx
import matplotlib.pyplot as plt
from collections import OrderedDict
import time
import functools

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

#path = ['AA', 'DD', 'open', 'CC', 'BB', 'open', 'AA', 'II', 'JJ', 'open', 'II', 'AA', 'DD', 'EE', 'FF', 'GG', 'HH', 'open', 'GG', 'FF', 'EE', 'open', 'DD', 'CC', 'open', ]

def closed_nonzero_valves(open_valves):
	return [v for v in valves if v not in open_valves and valves[v][0] != 0]

@functools.lru_cache(maxsize=None)
def path_to_valve(current, target):
	return nx.shortest_path(G, current, target)

def flow_per_step(open_valves):
	return sum(valves[v][0] for v in open_valves)

def new_wins(new_flow, new_steps_taken, new_node, sorted_new_open_valves, visited):
	visited_flow, visited_steps_taken = visited[new_node, sorted_new_open_valves]
	expected_new = new_flow + flow_per_step(new_open_valves)*(max_steps - new_steps_taken)
	expected_visited = visited_flow + flow_per_step(sorted_new_open_valves)*(max_steps - visited_steps_taken)
	return expected_new > expected_visited

max_steps = 26

current = 'AA'
open_valves = ()
steps_taken = 0
total_flow = 0

state = (current, open_valves, steps_taken, total_flow)

frontier = [state]
visited = {(current, open_valves): (total_flow, steps_taken)}

max_flow = 0

while len(frontier) > 0:
	#print(len(frontier), max_flow)
	current, open_valves, steps_taken, total_flow = frontier.pop()
	targets = closed_nonzero_valves(open_valves)
	if all([len(path_to_valve(current, target)) + steps_taken > max_steps for target in targets]):
		# no time to reach any of the closed valves
		final_flow = total_flow + flow_per_step(open_valves)*(max_steps - steps_taken)
		if final_flow > max_flow:
			max_flow = final_flow
			#print(open_valves, steps_taken, final_flow)
		continue

	for target in targets:
		path = path_to_valve(current, target)
		new_node = target
		new_steps_taken = steps_taken + len(path) - 1 # get to the valve
		new_steps_taken += 1 # open the valve
		new_total_flow = total_flow + flow_per_step(open_valves)*len(path)
		new_open_valves = open_valves + (target,)
		new_final_flow = new_total_flow + flow_per_step(new_open_valves)*(max_steps - new_steps_taken)
		sorted_new_open_valves = tuple(sorted(new_open_valves))
		if new_steps_taken > max_steps:
			continue
		if (new_node, sorted_new_open_valves) not in visited:
			frontier.append((new_node, new_open_valves, new_steps_taken, new_total_flow))
			visited[new_node, sorted_new_open_valves] = new_final_flow, new_steps_taken
		elif new_final_flow > visited[new_node, sorted_new_open_valves][0]:
			frontier.append((new_node, new_open_valves, new_steps_taken, new_total_flow))
			visited[new_node, sorted_new_open_valves] = new_final_flow, new_steps_taken
		
#print(len(visited))

visited_sets = [(set(v[1]), t[0]) for v, t in visited.items()]

max_combined_flow = max([t+t2 for v, t in visited_sets for v2, t2 in visited_sets if len(v.intersection(v2)) == 0])

print(max_combined_flow)

#print(time.perf_counter() - start_time) # 17 seconds