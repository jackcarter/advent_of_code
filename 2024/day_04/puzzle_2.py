with open("./data.txt") as data:
	lines = data.readlines()

def search_all_directions(lines, i, j):
	if i < 1 or j < 1 or i >= len(lines)-1 or j >= len(lines[i])-1:
		return False
	if lines[i][j] != 'A':
		return False
	first = lines[i-1][j-1] + lines[i+1][j+1]
	second = lines[i-1][j+1] + lines[i+1][j-1]
	if ''.join(sorted(first)) == 'MS' and ''.join(sorted(second)) == 'MS':
		return True
	return False

# convert lines to 2d array
lines = [line.strip() for line in lines]

count = 0
for i in range(len(lines)):
		for j in range(len(lines[i])):
			if search_all_directions(lines, i, j):
				count += 1
print(count)

