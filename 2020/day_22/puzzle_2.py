import itertools
from pprint import pprint

def score(cards):
	score = 0
	for ii, card in enumerate(cards[::-1]):
		score += (1+ii)*card
	return score

def hash_cards(cards1, cards2):
	#this is for making sure we don't infinite loop
	return "$".join(map(str,cards1)) + "#" + "$".join(map(str,cards2))

def play_game(cards1, cards2):
	game_states = set()
	while len(cards1) > 0 and len(cards2) > 0:
		game_state = hash_cards(cards1, cards2)
		if game_state in game_states:
			return "p1", [], []
		else:
			game_states.add(game_state)
		c1 = cards1.pop(0)
		c2 = cards2.pop(0)
		if c1 <= len(cards1) and c2 <= len(cards2):
			winner, x, y = play_game(cards1[:c1], cards2[:c2])
		else: 
			if c1 > c2:
				winner = "p1"
			elif c2 > c1:
				winner = "p2"
		if winner == "p1":
			cards1.extend([c1, c2])
		elif winner == "p2":
			cards2.extend([c2, c1])
	return winner, cards1, cards2

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

winner, cards1, cards2 = play_game(cards1, cards2)

if winner == "p1":
	print("Answer:", score(cards1))
else:
	print("Answer:", score(cards2))

# Answer: 35436