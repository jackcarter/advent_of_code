import itertools, functools

with open("data.txt") as data:
	packetpairs = data.read().split('\n\n')


def compare(a, b):
	if type(a) == int and type(b) == int:
		if a == b:
			return 0
		elif a > b:
			return 1
		else:
			return -1
	elif type(a) == int and type(b) == list:
		return compare([a], b)
	elif type(a) == list and type(b) == int:
		return compare(a, [b])
	elif type(a) == list and type(b) == list:
		for ai, bi in itertools.zip_longest(a, b):
			c = compare(ai, bi)
			if c == 0:
				continue
			else:
				return c
		return 0
	elif a is not None and b is None:
		return 1
	elif a is None and b is not None:
		return -1
	else:
		print('wtf')

packets = []
for i, pp in enumerate(packetpairs):
	p = pp.split('\n')
	packet1 = eval(p[0])
	packet2 = eval(p[1])
	packets.append(packet1)
	packets.append(packet2)

packets.append([[2]])
packets.append([[6]])

packets.sort(key=functools.cmp_to_key(compare))

x = packets.index([[2]]) + 1
y = packets.index([[6]]) + 1

print(x*y)