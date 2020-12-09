with open("data.txt") as data:
	lines = data.read().splitlines()
	lines = list(map(int, lines))

target=15690279
total = 0

start = 0
count = 1
while(total != target):
	total = sum(lines[start:start+count])
	if total < target:
		count += 1
	elif total > target:
		count = 1
		start += 1
	else:
		print(min(lines[start:start+count])+max(lines[start:start+count]))

# Answer: 2174232