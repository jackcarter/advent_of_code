from collections import defaultdict
import itertools

with open("data.txt") as data:
	lines = data.read().splitlines()

class Deer:
	def __init__(self, name, speed, flytime, resttime):
		self.name = name
		self.speed = speed
		self.flytime = flytime
		self.resttime = resttime

		self.flying = True
		self.time_remaining = flytime

		self.position = 0
		self.score = 0
	
	def fly(self):
		self.position += self.speed

	def start_flying(self):
		self.flying = True
		self.time_remaining = self.flytime
		self.fly()

	def start_resting(self):
		self.flying = False
		self.time_remaining = self.resttime

	def tick(self):
		if self.time_remaining == 0:
			if self.flying:
				self.start_resting()
			else:
				self.start_flying()
		else:
			if self.flying:
				self.fly()
				
		self.time_remaining -= 1

final_time = 2503
deers = []

for line in lines:
	words = line[:-1].split(' ')
	deers.append(Deer(words[0], int(words[3]), int(words[6]), int(words[-2])))

for second in range(final_time):
	for deer in deers:
		deer.tick()
	max_position = max(deers, key=lambda deer: deer.position).position
	for deer in deers:
		if deer.position == max_position:
			deer.score += 1

print(max(deers, key=lambda deer: deer.score).score)

# Answer: 1256