def valid(last_n, current):
	for i, n in enumerate(last_n):
		for j, m in enumerate(last_n):
			if j!=i and n+m==current:
				return True
	return False

groups = []
with open("data.txt") as data:
	lines = data.read().splitlines()
	lines = list(map(int, lines))

preamble = 25
lookback = 25
for ii in range(preamble, len(lines)):
	if valid(lines[ii-lookback:ii], lines[ii]):
		pass
	else:
		print(lines[ii])
		break

# Answer: 15690279