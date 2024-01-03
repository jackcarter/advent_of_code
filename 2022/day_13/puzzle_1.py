import itertools

with open("data.txt") as data:
	packetpairs = data.read().split('\n\n')


def compare(a, b):
	if type(a) == int and type(b) == int:
		if a == b:
			return None
		else:
			return a < b
	elif type(a) == int and type(b) == list:
		return compare([a], b)
	elif type(a) == list and type(b) == int:
		return compare(a, [b])
	elif type(a) == list and type(b) == list:
		for ai, bi in itertools.zip_longest(a, b):
			c = compare(ai, bi)
			if c is None:
				continue
			else:
				return c
	elif a is not None and b is None:
		#print(a, b)
		return False
	elif a is None and b is not None:
		return True
	else:
		print('wtf')

total = 0
for i, pp in enumerate(packetpairs):
	packets = pp.split('\n')
	packet1 = eval(packets[0])
	packet2 = eval(packets[1])
	if compare(packet1, packet2):
		total += (i+1)
print(total)