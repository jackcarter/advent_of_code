from itertools import combinations

with open("data.txt") as data:
	lines = data.read().splitlines()

containers = [int(line) for line in lines]
target = 150

combos = [combo for r in range(len(containers)) for combo in combinations(containers, r) if sum(combo) == target]
min_combo_len = min([len(combo) for combo in combos])
print(len([combo for combo in combos if len(combo) == min_combo_len]))