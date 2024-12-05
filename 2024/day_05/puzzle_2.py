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

def is_valid_update(up):
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
			return False
		seen.add(page)
	return True

def order_pages(up):
	seen = set()
	for i in range(len(up)):
		if up[i] in page_order:
			for p in page_order[up[i]]:
				if p not in seen and p in up:
					# invalid update
					up_valid = False
					initially_ordered = False
					# swap the two pages
					new_up = up.copy()
					new_up[i], new_up[up.index(p)] = new_up[up.index(p)], new_up[i]
					up = new_up.copy()
					return order_pages(up)
		seen.add(up[i])
	return up

sum_middles = 0
for up in update_pages:	
	if is_valid_update(up):
		pass # do not add middle page
	else:
		ordered_up = order_pages(up)
		middle_page = ordered_up[len(ordered_up) // 2]
		sum_middles += int(middle_page)

print(sum_middles)