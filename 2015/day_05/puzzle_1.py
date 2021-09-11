import string

with open("data.txt") as data:
	lines = data.readlines()


def is_nice(word):
	vowels = "aeiou"
	count_vowels = 0
	for c in word:
		if c in vowels:
			count_vowels += 1
	if count_vowels < 3:
		return False

	doubled = [ch + ch for ch in string.ascii_lowercase]
	for d in doubled:
		if d in word:
			break
	else:
		return False

	bad_strings = ["ab", "cd", "pq", "xy"]
	for bs in bad_strings:
		if bs in word:
			return False

	return True

count_nice = 0
for ii, line in enumerate(lines):
	if is_nice(line):
		count_nice += 1
print(count_nice)

# Answer: 236