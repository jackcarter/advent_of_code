import re

with open("data.txt") as data:
	lines = data.read().splitlines()

containers = {i: int(line) for i, line in enumerate(lines)}
target = 150

successes = []
tries = []

def build_containers(used, available):
	tries.append(sorted(list(used.keys())))
	#base conditions
	if sum(used.values()) == target:
		if used.keys() not in successes:
			print("success", used.keys())
			successes.append(used.keys())
	elif len(available) == 0:
		pass
	elif sum(used.values()) > target:
		pass
	else:
		for k, v in available.items():
			if sum(used.values()) + v <= target:
				new_used = used.copy()
				new_used[k] = v
				if sorted(list(new_used.keys())) not in tries:
					new_available = available.copy()
					del new_available[k]
					build_containers(new_used, new_available)

build_containers({}, containers)
print(len(successes))