import math, itertools

with open("data.txt") as data:
	lines = data.read().splitlines()

target = int(lines[0])

def getDivs(N):
    # https://stackoverflow.com/a/70635601/662761
    factors = {1}
    maxP  = int(N**0.5)
    p,inc = 2,1
    while p <= maxP:
        while N%p==0:
            factors.update([f*p for f in factors])
            N //= p
            maxP = int(N**0.5)
        p,inc = p+inc,2
    if N>1:
        factors.update([f*N for f in factors])
    return sorted(factors)

def num_presents(n):
    return 10*sum(getDivs(n))

record = -1
ii = 1
while True:
	ii += 1
	ap = num_presents(ii)
	if ap > record:
		record = ap
	if ap >= target:
		print(ii)
		break