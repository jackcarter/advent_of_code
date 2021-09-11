with open("data.txt") as data:
	lines = data.readlines()
	for ii, line in enumerate(lines):
		num1 = int(line)
		for jj, line2 in enumerate(lines):
			num2=int(line2)
			if ii!=jj and num1+num2==2020:
				print(num1*num2)
				break
# Answer: 776064