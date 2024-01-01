with open("data.txt") as data:
	lines = data.read()

distinct_chars_for_marker = 14

for i, _ in enumerate(lines):
	if len(set(lines[i:i+distinct_chars_for_marker])) == distinct_chars_for_marker:
		print(i+distinct_chars_for_marker)
		break