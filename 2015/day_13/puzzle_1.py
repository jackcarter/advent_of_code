from collections import defaultdict
import itertools

with open("data.txt") as data:
	lines = data.read().splitlines()

guests = defaultdict(dict)
happiness = {}

for line in lines:
	words = line[:-1].split(' ')
	sign = 1 if words[2] == 'gain' else -1
	guests[words[0]][words[-1]] = int(words[3])*sign

def calc(guests, sequence):
	looped_sequence = list(sequence)
	looped_sequence.append(looped_sequence[0])
	looped_sequence.append(looped_sequence[1])
	total_happiness = 0
	for ii in range(1,len(sequence)+1):
		total_happiness += guests[looped_sequence[ii]][looped_sequence[ii+1]]
		total_happiness += guests[looped_sequence[ii]][looped_sequence[ii-1]]
	return total_happiness

max_happiness = 0
sequences = itertools.permutations(list(guests.keys()))
for seq in sequences:
	max_happiness = max(max_happiness, calc(guests,seq))
print(max_happiness)

# Answer: 664