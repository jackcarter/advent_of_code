from copy import deepcopy

def parse_line(line):
	ins, num = line.split(" ")
	num = int(num)
	return ins, num

def hash_addr(address):
	return str(address[0]) + "$" + str(address[1])


with open("data.txt") as data:
	#lines = list(map(int, data.read().splitlines()))
	lines = data.read().splitlines()

dirs = ['ne', 'e', 'se', 'sw', 'w', 'nw']



tiles = {}

for data in lines:
	address = [0,0]
	instructions = []
	pointer = 0
	while pointer < len(data):
		if pointer < len(data)-1 and data[pointer] + data[pointer+1] in dirs:
			instructions.append(data[pointer] + data[pointer+1])
			pointer += 2
		else:
			instructions.append(data[pointer])
			pointer += 1
	#print(instructions)
	for ins in instructions:
		if ins=='ne':
			address[0]+=0
			address[1]+=1
		elif ins=='e':
			address[0]+=1
			address[1]+=0
		elif ins=='se':
			address[0]+=1
			address[1]+=-1
		elif ins=='sw':
			address[0]+=0
			address[1]+=-1
		elif ins=='w':
			address[0]+=-1
			address[1]+=0
		elif ins=='nw':
			address[0]+=-1
			address[1]+=1
		#print(ins, address)
	#print(address)
	addr_str = hash_addr(address)
	if addr_str not in tiles:
		tiles[addr_str] = 'b'
		#print("new black", addr_str)
	else:
		if tiles[addr_str] == 'b':
			#print("black to white", addr_str)
			tiles[addr_str] = 'w'
		elif tiles[addr_str] == 'w':
			#print("white to black", addr_str)
			tiles[addr_str] = 'b'

black = len([v for k, v in tiles.items() if v=='b'])

def count_black_neighbors(tiles, ii, jj):
	dirs = [[0,1], [1,0], [1,-1], [0,-1], [-1,0], [-1,1]]
	count_black = 0
	for d in dirs:
		check_addr_str = hash_addr([ii+d[0], jj+d[1]])
		if check_addr_str in tiles:

			if tiles[check_addr_str] == 'b':
				count_black += 1
		else:
			tiles[check_addr_str] = 'w'
	return count_black


domain = 30

for ii in range(-domain,domain):
	for jj in range(-domain,domain):
		ref_tile = hash_addr([ii,jj])
		if ref_tile not in tiles:
			tiles[ref_tile] = 'w'

domain -= 5

for day in range(1, 101):
	max_ii = 10
	max_jj = 10
	new_tiles = deepcopy(tiles)
	for ii in range(-domain,domain):
		for jj in range(-domain,domain):
			ref_tile = hash_addr([ii,jj])
			bn = count_black_neighbors(tiles, ii, jj)
			if ref_tile not in tiles:
				tiles[ref_tile] = 'w'
			if tiles[ref_tile] == 'w':
				if bn == 2:
					if abs(ii) > max_ii:
						max_ii = abs(ii)
					if abs(jj) > max_jj:
						max_jj = abs(jj)
					new_tiles[ref_tile] = 'b'
			else:
				if abs(ii) > max_ii:
					max_ii = abs(ii)
				if abs(jj) > max_jj:
					max_jj = abs(jj)

				if bn == 0 or bn > 2:
					new_tiles[ref_tile] = 'w'
	tiles = deepcopy(new_tiles)
	domain = max(max_ii, max_jj) + 10
	
print("Answer:", len([v for k, v in new_tiles.items() if v=='b']))

# Answer: 3711