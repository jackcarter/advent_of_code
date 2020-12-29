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
pprint(allergen_dict)
pprint(ingredients_set)
print([v for k, v in allergen_dict.items()])
remaining_ingredients = set.union(*[v for k, v in allergen_dict.items()])
safe_ingredients = ingredients_set - remaining_ingredients
total_count = 0
for si in safe_ingredients:
	total_count+=ingredient_counts[si]
print(total_count)
# Answer: 1707