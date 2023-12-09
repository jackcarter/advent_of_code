import re
from operator import itemgetter
with open("./data.txt") as data:
	lines = data.read().splitlines()

def d(l):
	return [int(l[i]) - int(l[i-1]) for i in range(1,len(l))]
	
news = []
for line in lines:
	diffs = [[int(i) for i in line.split(' ')]]
	diffs.append(d(diffs[-1]))
	while any([d != 0 for d in diffs[-1]]):
		diffs.append(d(diffs[-1]))
	diffs.reverse()
	for ii in range(len(diffs)-1):
		new = diffs[ii+1][0] - diffs[ii][0]
		diffs[ii+1].insert(0, new)
	news.append(new)
print(sum(news))