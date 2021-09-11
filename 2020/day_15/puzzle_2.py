import itertools
from pprint import pprint

with open("data.txt") as data:
	lines = data.read().splitlines()

nums = list(map(int,lines[0].split(",")))

last_used = {nums[ii]:ii for ii in range(len(nums))}

old_speak = nums[-1]
for ii in range(len(nums), 30000000):
	if old_speak not in last_used:
		#print("fdsa", speak, last_used[speak], ii)
		new_speak = 0
	else:
		new_speak = ii - 1 - last_used[old_speak]
		#last_used[speak] = ii
	last_used[old_speak] = ii - 1
	#print(new_speak)
	old_speak = new_speak

print("Answer:",new_speak)

# Answer: 11721679