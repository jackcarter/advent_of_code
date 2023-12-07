import math
with open("./data.txt") as data:
	lines = data.read().splitlines()

time = int("".join([i for i in lines[0].split(" ") if i.isdigit()]))
distance = int("".join([i for i in lines[1].split(" ") if i.isdigit()]))

#time*t-t**2 = distance
#t**2 - time*t + distance = 0
#t = 1/2*(time ± sqrt(time**2-4*distance))

t1 = (time - math.sqrt((time)**2 - 4*distance))/2
t2 = (time + math.sqrt((time)**2 - 4*distance))/2

print(math.floor(t2)-math.ceil(t1)+1)