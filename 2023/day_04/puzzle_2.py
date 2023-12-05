with open("./data.txt") as data:
	lines = data.readlines()

def parse_lines(lines):
	cards = {}
	for line in lines:
		line = line.replace('  ', ' ')
		line = line.replace('\n', '')
		card_num = ''.join(c for c in line.split(': ')[0] if c.isdigit())
		trimmed = line.split(': ')[1]
		winners = trimmed.split(' | ')[0].split(' ')
		numbers = trimmed.split(' | ')[1].split(' ')
		cards[int(card_num)] = {"winners": winners, "numbers": numbers, "copies": 1}
	return cards

def get_number_of_copies(card):
	matches = len([n for n in card["numbers"] if n in card["winners"]])
	return matches

cards = parse_lines(lines)

max_card_num = max([k for k,v in cards.items()])

for card_num in range(1, max_card_num+1):
	copies = get_number_of_copies(cards[card_num])
	for ii in range(copies):
		cards[card_num + ii + 1]["copies"] += cards[card_num]["copies"]

print(sum([card["copies"] for card in cards.values()]))