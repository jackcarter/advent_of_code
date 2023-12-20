with open("data.txt") as data:
	lines = data.read().splitlines()

def get_loop_size(target):
	counter = 0
	num = 1
	while num != target:
		num = num * 7
		num = num % 20201227
		counter += 1
	return counter

dpk = int(lines[0])
cpk = int(lines[1])

card_loop_size = get_loop_size(cpk)

num = 1
for ii in range(card_loop_size):
	num = num * dpk
	num = num % 20201227
print("Answer:", num) 

# Answer: 448851