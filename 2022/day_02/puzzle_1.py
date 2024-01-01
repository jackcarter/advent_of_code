with open("data.txt") as data:
	lines = data.read().splitlines()

shapescores = {'A': 1, 'B': 2, 'C': 3, }
convert = {'X': 'A', 'Y': 'B', 'Z': 'C'}

def score(op, me):
	shapescore = shapescores[convert[me]]
	winner = (shapescores[convert[me]] - shapescores[op] + 1) % 3
	return shapescore + winner*3

print(sum([score(*line.split(' ')) for line in lines]))