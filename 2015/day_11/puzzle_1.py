import string

with open("data.txt") as data:
	lines = data.read().splitlines()

password = lines[0]

password = [l for l in password] # convert to list so that we can edit in-place

class Password:
	def __init__(self, password):
		self.val = [l for l in password] # convert to list so that we can edit in-place

	def password(self):
		return ''.join(self.val)

	def increment(self):
		for ii, letter in enumerate(self.val[::-1]):
			if letter != 'z':
				self.val[-(ii+1)] = chr(ord(letter)+1)
				break
			else:
				self.val[-(ii+1)] = 'a'

	def check_valid(self):
		# First check for straights
		straights = [ch + chr(ord(ch)+1) + chr(ord(ch)+2) for ch in string.ascii_lowercase if ord(ch) < ord('y')]
		for s in straights:
			if s in self.password():
				break
		else:
			return False

		for ch in "iol":
			if ch in self.password():
				return False

		count_doubled = 0
		for ii in range(1, len(self.val)):
			if self.val[ii] == self.val[ii-1]:
				if ii > 2 and self.val[ii] == self.val[ii-2]:
					# 3-in-a-row doesn't count as two pairs
					continue
				count_doubled += 1
		if count_doubled < 2:
			return False

		return True
			
password = Password(lines[0])

while not password.check_valid():
	password.increment()

print(password.password())

# Answer: cqjxxyzz