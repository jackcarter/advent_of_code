with open("./data.txt") as data:
	lines = data.readlines()
	sum = 0
	list_str_numbers = ['one','two','three','four','five','six','seven','eight','nine']
	digits = ["%1d" %i for i in range(1,10)] + list_str_numbers
	for line in lines:
		first = ''
		earliest = 9999
		last = ''
		latest = -1
		for digit in digits:
			index = line.find(digit)
			if index > -1 and index < earliest:
				first = digit
				earliest = index
			index = line.rfind(digit)
			if index > -1 and index > latest:
				last = digit
				latest = index
		if first in list_str_numbers:
			first = list_str_numbers.index(first) + 1
		if last in list_str_numbers:
			last = list_str_numbers.index(last) + 1
		sum += int(first)*10 + int(last)
	print(sum)