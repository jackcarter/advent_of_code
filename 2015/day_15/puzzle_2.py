import re
import numpy as np
import math

with open("data.txt") as data:
	lines = data.read().splitlines()

numbers = []
for line in lines:
	numbers.append([int(i) for i in re.findall(r'-?\d+', line)])
ingredients = np.array(numbers)
maxscore = 0
optimal_amounts = []
for ii in range(101):
	print(ii)
	for jj in range(101):
		for kk in range(101):
			for ll in range(101):
				if ii + jj + kk + ll == 100:
					amounts = [ii,jj,kk,ll]
					totals = np.matmul(amounts, ingredients[:,:-1])
					total_calories = np.matmul(amounts, ingredients[:,-1])
					if total_calories == 500:
						totals = [0 if i < 0 else i for i in totals]
						score = math.prod(totals)
						if score > maxscore:
							maxscore = score
							optimal_amounts = amounts
print(optimal_amounts)
print(maxscore)