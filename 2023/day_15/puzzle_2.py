from collections import OrderedDict

with open("./data.txt") as data:
	lines = data.read().split(',')

boxes = [OrderedDict() for i in range(256)]

def get_hash(string):
	subtotal = 0
	for c in string:
		subtotal = ((subtotal+ord(c))*17) % 256
	return subtotal

total = 0
for line in lines:
	if '=' in line:
		label, lens = line.split('=')
		box_id = get_hash(label)
		if label in boxes[box_id].keys():
			boxes[box_id][label] = int(lens)
		else:
			boxes[box_id][label] = int(lens)
	else:
		label = line[:-1]
		box_id = get_hash(label)
		if label in boxes[box_id].keys():
			boxes[box_id].pop(label)
for ii, box in enumerate(boxes):
	for jj, value in enumerate(box.values()):
		total += (ii+1)*(jj+1)*value

print(total)