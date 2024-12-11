from collections import defaultdict

with open("./data.txt") as data:
	line = data.read()

stones=line.split()

def get_stone_counts(stone, memo=None):
		if memo is None:
				memo = {}
		
		if stone in memo:
				return memo[stone].copy()
		
		if stone == '0':
			new_stones = ['1']
		elif len(stone) % 2 == 0:
			new_stones = [str(int(stone[:len(stone)//2])), str(int(stone[len(stone)//2:]))]
		else:
			new_stones = [str(int(stone)*2024)]
		memo[stone] = new_stones.copy()
		return new_stones

memo = {}
stone_counts = defaultdict(int)
for stone in stones:
		stone_counts[stone] = 1

for i in range(75):
	new_counts = defaultdict(int)
	for stone, count in stone_counts.items():
		transformed = get_stone_counts(stone, memo)
		for new_stone in transformed:
			new_counts[new_stone] += count
	
	stone_counts = new_counts
	
print(sum(stone_counts.values()))