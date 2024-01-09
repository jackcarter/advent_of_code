import re
import networkx as nx
import matplotlib.pyplot as plt
from collections import OrderedDict
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

@functools.lru_cache(maxsize=None)
def solve(steps_remaining, valves_remaining, my_current, elephant_current):
	print("start", steps_remaining, sorted(valves_remaining), my_current, elephant_current)
	steps_taken = 0
	final_flows = [0]

	if steps_remaining == 0:
		return 0
	if len(valves_remaining) == 0:
		return 0
	elif len(valves_remaining) == 1:
		targets = [(valves_remaining[0], None), (None, valves_remaining[0])]
	else:
		targets = list(itertools.permutations(valves_remaining, 2))

	if all([len(path_to_valve(my_current, my_target)) + steps_taken > steps_remaining \
		 and len(path_to_valve(elephant_current, elephant_target)) + steps_taken > steps_remaining \
		 for my_target, elephant_target in targets]):
		# no time to reach any of the closed valves
		return 0
	
	for my_target, elephant_target in targets:
		newly_opened_valves = []
		new_steps_remaining = steps_remaining
		#print(my_target, elephant_target)
		# pick targets
		my_path = path_to_valve(my_current, my_target)
		elephant_path = path_to_valve(elephant_current, elephant_target)

		# we'll only advance until at least one of us reaches our target
		len_shortest_path = min(len(my_path), len(elephant_path))

		if len_shortest_path + 1 > new_steps_remaining:
			# we can't reach our target and turn on valve
			continue

		# figure out where we end up before the last step (turning on at least one valve)
		my_new_node = my_path[len_shortest_path - 1]
		elephant_new_node = elephant_path[len_shortest_path - 1]

		# decrement steps for the walking
		new_steps_remaining -= len_shortest_path - 1
		# open the valve and walk one more step (or open both valves)
		new_steps_remaining -= 1 

		if my_new_node == my_target:
			newly_opened_valves.append(my_target)
		else:
			my_new_node = my_path[len_shortest_path]
		if elephant_new_node == elephant_target:
			newly_opened_valves.append(elephant_target)
		else:
			elephant_new_node = elephant_path[len_shortest_path]

		# next, solve from this new position. Add result of solving to total flow and return
		new_valves_remaining = tuple(sorted([v for v in valves_remaining if v not in newly_opened_valves]))
		if len(new_valves_remaining) == 0:
			new_flow = 0
		else:
			new_flow = solve(new_steps_remaining, new_valves_remaining, my_new_node, elephant_new_node)
		#print(new_flow, new_steps_remaining)
		final_flows.append(flow_per_step(newly_opened_valves)*new_steps_remaining + new_flow)

	#print(steps_remaining, sorted(valves_remaining), my_current, elephant_current, max(final_flows))
	return max(final_flows)

#print(solve(26, tuple(set(nonzero_valves)-set(['BB','CC','DD'])), 'AA', 'AA'))

print(solve(max_steps, nonzero_valves, current, elephant_current))