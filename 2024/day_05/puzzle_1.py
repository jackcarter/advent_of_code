with open("./data.txt") as data:
	lines = data.read().splitlines()

page_order = {}
update_pages = []
after_break = False
for line in lines:
	if line == "":
		after_break = True
		continue
	if after_break:
		update_pages.append(line.split(","))
	else:
		s = line.split("|")
		if s[1] in page_order:
			page_order[s[1]].append(s[0])
		else:
			page_order[s[1]] = [s[0]]

sum_middles = 0
for up in update_pages:
	seen = set()
	for page in up:
		up_valid = True
		if page in page_order:
			for p in page_order[page]:
				if p not in seen and p in up:
					# invalid update
					up_valid = False
					break
		if not up_valid:
			break
		seen.add(page)
	else:
		# valid update
		# get middle page number
		middle_page = up[len(up) // 2]
		sum_middles += int(middle_page)
print(sum_middles)