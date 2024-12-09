import math

with open("./data.txt") as data:
	lines = data.read().splitlines()

expanded = []
file_ind = True
file_id = 0
for char in lines[0]:
	if file_ind:
		expanded.extend([file_id]*int(char))
		file_id += 1
	else:
		expanded.extend(['.']*int(char))
	file_ind = not file_ind
#print(''.join([str(c) for c in expanded]))

# now make 2 pointers to fill in the dots
left = 0
right = 0
length = len(expanded)
checksum = 0
while right + left < length:
	# move left to the next dot
	if expanded[left] != '.':
		checksum += left*expanded[left]
		left += 1
	elif expanded[length-1-right] != '.':
		checksum += left*expanded[length-1-right]
		right += 1
		left += 1
	else:
		right += 1
print(checksum)