import re

with open("data.txt") as data:
    rc = re.findall(r'\d+', data.read())
    r = int(rc[0])
    c = int(rc[1])

def tri(n):
    return (n+1)*n//2

n = tri(c) + tri(c+r-2)-tri(c-1)

num = 20151125
for i in range(1, n):
    num = (num *252533) % 33554393
print(num)