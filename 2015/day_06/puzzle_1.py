import re

with open("data.txt") as data:
	lines = data.read().splitlines()

class Grid:
	side_length = 1000

	def __init__(self):
		self.lights = [[False for ii in range(self.side_length)] for jj in range(self.side_length)]

	def _apply_to_rectangle(self, c1, c2, r1, r2, func):
		for cc in range(c1,c2+1):
			for rr in range(r1,r2+1):
				self.lights[cc][rr] = func(self.lights[cc][rr])

	def off(self, c1, c2, r1, r2):
		self._apply_to_rectangle(c1,c2,r1,r2,lambda x: False)

	def on(self, c1, c2, r1, r2):
		self._apply_to_rectangle(c1,c2,r1,r2,lambda x: True)

	def toggle(self, c1, c2, r1, r2):
		self._apply_to_rectangle(c1,c2,r1,r2,lambda x: not x)

	def count_on(self):
		count = 0
		for col in self.lights:
			for light in col:
				if light:
					count += 1
		return count

grid = Grid()

for line in lines:
	matches = re.findall(r"\d+", line)
	c1 = int(matches[0])
	r1 = int(matches[1])
	c2 = int(matches[2])
	r2 = int(matches[3])
	if "toggle" in line:
		grid.toggle(c1, c2, r1, r2)
	elif "turn on" in line:
		grid.on(c1, c2, r1, r2)
	elif "turn off" in line:
		grid.off(c1, c2, r1, r2)
		
print(grid.count_on())

# Answer: 543903