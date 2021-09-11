from hashlib import md5

with open("data.txt") as data:
	lines = data.readlines()

secret = lines[0]

for ii in range(10000000):
	md5hash = md5((secret + str(ii)).encode()).hexdigest()
	if md5hash[:6] == '000000':
		print(ii)
		break


# Answer: 9958218