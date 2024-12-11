with open("./data.txt") as data:
	line = data.read()

stones=line.split()

for i in range(25):
	new_stones = []
	for stone in stones:
		if stone == '0':
			new_stones.append('1')
		elif len(stone) % 2 == 0:
			new_stones.extend([str(int(stone[:len(stone)//2])), str(int(stone[len(stone)//2:]))])
		else:
			new_stones.append(str(int(stone)*2024))
	stones = new_stones.copy()
print(len(stones))