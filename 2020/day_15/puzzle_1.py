import itertools
from pprint import pprint

with open("data.txt") as data:
	lines = data.read().splitlines()

nums = list(map(int,lines[0].split(",")))

def get_last_occurrence(nums, item):
	nums.reverse()
	return len(nums) - nums.index(item) - 1

for ii in range(2020):
	if ii < len(nums):
		pass
	else:
		last_spoken = nums[ii-1]
		if last_spoken in nums[:ii-1]:
			last_index = get_last_occurrence(nums[:-1], last_spoken)
			next_num = ii - 1 - last_index
			nums.append(next_num)
		else:
			nums.append(0)
print("Answer:", nums[-1])

# Answer: 447