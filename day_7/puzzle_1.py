def get_containing_bags(bags, start_bag):
	top_bags = []
	for name, contents in bags.items():
		if start_bag in contents:
			top_bags.append(name)
			top_bags.extend(get_containing_bags(bags, name))
	return top_bags

def parse_line(line):
	name, contents_txt = line.split(" bags contain ")
	contents = {}
	contents_txt = contents_txt[:-1] #drop the period
	if contents_txt == "no other bags":
		contents = []
	else:
		csplit = contents_txt.split(", ")
		for x in csplit:
			content_desc = x.split(" ")
			num = content_desc[0]
			content_bag_name = content_desc[1]+" "+content_desc[2]
			contents[content_bag_name] = num
	return name, contents

groups = []
with open("data.txt") as data:
	lines = data.read().splitlines()

bags = {}
for line in lines:
	name, contents = parse_line(line)
	bags[name] = contents

top_level_bags = get_containing_bags(bags, "shiny gold")

#print(top_level_bags)
print(len(set(top_level_bags)))

# Answer: 287