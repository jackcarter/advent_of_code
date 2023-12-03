with open("./data.txt") as data:
	lines = data.readlines()

def game_power(line):
	games = line.split(": ")[1].split(";")
	red = 0
	green = 0
	blue = 0
	for game in games:
		colors = game.split(",")
		for color in colors:
			count = [int(i) for i in color.split() if i.isdigit()][0]
			if "red" in color:
				if count > red:
					red = count
			elif "green" in color:
				if count > green:
					green = count
			elif "blue" in color:
				if count > blue:
					blue = count
			else:
				pass
	return red*green*blue


print(sum([game_power(line) for line in lines]))