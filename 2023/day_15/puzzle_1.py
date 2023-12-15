with open("./data.txt") as data:
	lines = data.read().split(',')

def get_hash(string):
	subtotal = 0
	for c in string:
		subtotal = ((subtotal+ord(c))*17) % 256
	return subtotal

total = 0
for line in lines:
	total += get_hash(line)
print(total)