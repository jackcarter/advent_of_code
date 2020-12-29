import itertools
from pprint import pprint

def score(cards):
	score = 0
	for ii, card in enumerate(cards[::-1]):
		score += (1+ii)*card
	return score

with open("data.txt") as data:
	lines = data.read().splitlines()

cards1 = []
cards2 = []
adding_cards_to = cards1
for line in lines:
	if line in ["", "Player 1:"]:
		continue
	elif line == "Player 2:":
		adding_cards_to = cards2
		continue
	adding_cards_to.append(int(line))

while len(cards1) > 0 and len(cards2) > 0:
	c1 = cards1.pop(0)
	c2 = cards2.pop(0)
	if c1 > c2:
		cards1.extend([c1, c2])
	elif c2 > c1:
		cards2.extend([c2, c1])

if len(cards1) > 0:
	print("Answer:", score(cards1))
else:
	print("Answer:", score(cards2))
# Answer: 31754