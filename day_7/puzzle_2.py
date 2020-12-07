def get_contained_bags(bags, start_bag):
	total_bags = 0
	for contained_bag in bags[start_bag]:
		num_contained_bags = int(bags[start_bag][contained_bag])
		total_bags += num_contained_bags
		total_bags += num_contained_bags*get_contained_bags(bags, contained_bag)
	return total_bags

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

contained_bags = get_contained_bags(bags, "shiny gold")

print(contained_bags)

# Answer: 48160