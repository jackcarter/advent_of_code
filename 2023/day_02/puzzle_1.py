with open("./data.txt") as data:
	lines = data.readlines()

def game_possible(line):
	games = line.split(": ")[1].split(";")
	for game in games:
		colors = game.split(",")
		for color in colors:
			count = [int(i) for i in color.split() if i.isdigit()][0]
			if "red" in color:
				if int(count) > 12: return False
			elif "green" in color:
				if int(count) > 13: return False
			elif "blue" in color:
				if int(count) > 14: return False
			else:
				pass
	return True


print(sum([ii+1 for ii, line in enumerate(lines) if game_possible(line)]))