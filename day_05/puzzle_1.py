def get_seat_id(seat):
	row = seat[:7].replace("F","0").replace("B","1")
	col = seat[7:].replace("L","0").replace("R","1")
	return int(row+col,2)

with open("data.txt") as data:
	lines = data.read().splitlines()

seat_ids = []
for line in lines:
	seat_ids.append(get_seat_id(line))

print(max(seat_ids))

# Answer: 922