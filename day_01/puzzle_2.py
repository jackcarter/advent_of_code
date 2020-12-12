with open("data.txt") as data:
	lines = data.readlines()
	for ii, line in enumerate(lines):
		num1 = int(line)
		for jj, line2 in enumerate(lines):
			num2=int(line2)
			for kk, line3 in enumerate(lines):
				num3=int(line3)
				if ii!=jj and jj!=kk and ii!=kk and num1+num2+num3==2020:
					print(num1*num2*num3)
					break
# Answer: 6964490