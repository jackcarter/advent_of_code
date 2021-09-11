import itertools
from pprint import pprint

def parse_line(line):
	ing_str, aller_str = line.split(" (contains ")
	ingredients = set(ing_str.split(" "))
	allergens = aller_str[:-1].split(", ")
	return allergens, ingredients

with open("data.txt") as data:
	lines = data.read().splitlines()

allergen_dict = {}
ingredients_set = set()
ingredient_counts = {}
for ii, line in enumerate(lines):
	allergens, ingredients = parse_line(line)
	for allergen in allergens:
		if allergen not in allergen_dict:
			allergen_dict[allergen] = set(ingredients)
		else:
			allergen_dict[allergen] = allergen_dict[allergen].intersection(ingredients)
	ingredients_set = ingredients_set.union(ingredients)
	for ingredient in ingredients:
		if ingredient not in ingredient_counts:
			ingredient_counts[ingredient] = 1
		else:
			ingredient_counts[ingredient] += 1
			
ad2 = {}
while len(ad2) < len(allergen_dict):
	for allergen in allergen_dict:
		if len(allergen_dict[allergen]) == 1:
			ingredient_to_remove = next(iter(allergen_dict[allergen]))
			ad2[allergen] = ingredient_to_remove
			for allergen in allergen_dict:
				if ingredient_to_remove in allergen_dict[allergen] and len(allergen_dict[allergen]) > 1:
					allergen_dict[allergen].remove(ingredient_to_remove)

#invert dictionary
inverted = ",".join([v for k, v in sorted(ad2.items(), key=lambda item: item[0])])
print("Answer:",inverted)

# Answer: ntft,nhx,kfxr,xmhsbd,rrjb,xzhxj,chbtp,cqvc