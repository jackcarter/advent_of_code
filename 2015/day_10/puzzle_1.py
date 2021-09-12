with open("data.txt") as data:
	lines = data.read().splitlines()

sequence = lines[0]

def next_sequence(sequence):
	last_seen = sequence[0]
	current_count = 0
	next_sequence = ""
	for char in sequence:
		if char == last_seen:
			current_count += 1
		else:
			next_sequence += str(current_count) + last_seen
			current_count = 1
			last_seen = char
	next_sequence += str(current_count) + last_seen
	return next_sequence

for ii in range(40):
	sequence = next_sequence(sequence)

print(len(sequence))

# Answer: 329356