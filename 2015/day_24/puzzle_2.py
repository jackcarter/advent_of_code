import itertools
import math

with open("data.txt") as data:
    packages = set([int(l) for l in data.read().splitlines()])

total = sum(packages)
target = total // 4

package_groups = []

# find groups that sum to target
for i in range(1, len(packages)):
    if package_groups:
        break
    for group in itertools.combinations(packages, i):
        if sum(group) == target:
            package_groups.append(group)

package_groups.sort(key=lambda x: math.prod(x))

for group1 in package_groups:
    remaining_packages = set(packages - set(group1))
    for i in range(1, len(remaining_packages)):
        for group2 in itertools.combinations(remaining_packages, i):
            if sum(group2) == target:
                for j in range(1, len(remaining_packages) - i):
                    for group3 in itertools.combinations(remaining_packages-set(group2), j):
                        group4 = remaining_packages - set(group2) - set(group3)
                        if sum(group3) == target and sum(group4) == target:
                            print(math.prod(group1))
                            exit(0)