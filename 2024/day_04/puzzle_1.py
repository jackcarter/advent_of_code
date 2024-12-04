with open("./data.txt") as data:
	lines = data.readlines()

def search_word(lines, i, j, word, direction):
	if i < 0 or j < 0 or i >= len(lines) or j >= len(lines[i]):
		return False
	if word[0] != lines[i][j]:
		return False
	if len(word) == 1:
		return True
	return search_word(lines, i + direction[0], j + direction[1], word[1:], direction)

def search_all_directions(lines, i, j, word):
	directions = [
		(0, 1), # right
		(1, 1), # bottom right
		(1, 0), # bottom
		(1, -1), # bottom left
		(0, -1), # left
		(-1, -1), # top left
		(-1, 0), # top
		(-1, 1) # top right
	]
	count = 0
	for direction in directions:
		if search_word(lines, i, j, word, direction):
			count += 1
	return count

# convert lines to 2d array
lines = [line.strip() for line in lines]

count = 0
for i in range(len(lines)):
		for j in range(len(lines[i])):
			count += search_all_directions(lines, i, j, "XMAS")
print(count)

