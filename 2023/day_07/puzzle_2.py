import re
from operator import itemgetter
with open("./data.txt") as data:
	lines = data.read().splitlines()

def score(h):
	card_count = {}
	for c in h:
		if c in card_count:
			card_count[c] += 1
		else:
			card_count[c] = 1
	
def get_counts(hand):
	return [(c,len(re.findall(c, hand))) for c in ''.join(set(hand)) if c != 'J']

def two_pair(counts):
	pairs = 0
	for c in counts:
		if c[1] == 2:
			pairs += 1
	return pairs == 2

all_cards = ['1','J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']

def get_score(cards):
	counts = get_counts(cards)
	jokercount = len(re.findall('J', cards))
	maxcount = max([c[1] for c in counts])
	for ii, c in enumerate(counts):
		if c[1] == maxcount:
			counts[ii] = (counts[ii][0], counts[ii][1] + jokercount)
			break
	if any([c[1]==5 for c in counts]):
		score = 7*10**10 #5 of a kind
	elif any([c[1]==4 for c in counts]):
		score = 6*10**10 #4 of a kind
	elif any([c[1]==3 for c in counts]) and any([c[1]==2 for c in counts]):
		score = 5*10**10 #full house
	elif any([c[1]==3 for c in counts]):
		score = 4*10**10 #3 of a kind
	elif two_pair(counts):
		score = 3*10**10 #two pair
	elif any([c[1]==2 for c in counts]):
		score = 2*10**10 #pair
	else:
		score = 1*10**10 #high card
	for ii, card in enumerate(cards):
		addend = (all_cards.index(card)+1)*16**(len(cards)-ii)
		score += addend
	return score

hands = []
for line in lines:
	hand, bid = line.split(' ')
	if hand == 'JJJJJ':
		hand = '11111'
	hands.append((hand, bid, get_score(hand)))

hands.sort(key=itemgetter(2))

winnings = 0
for ii, hand in enumerate(hands):
	rank = ii+1
	winnings += rank*int(hand[1])
print(winnings)
