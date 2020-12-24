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
			print("black to white", addr_str)
			tiles[addr_str] = 'w'
		elif tiles[addr_str] == 'w':
			print("white to black", addr_str)
			tiles[addr_str] = 'b'

black = len([v for k, v in tiles.items() if v=='b'])
print("Answer:",black)

# Answer: 330