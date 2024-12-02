with open("./data.txt") as data:
	lines = data.readlines()

safe_reports = 0
for line in lines:
	asc = None
	items = line.split()
	for i in range(len(items)):
		cur = int(items[i])
		if i == 0:
			continue
		prev = int(items[i-1])
		if cur > prev:
			if asc == None:
				asc = True
			elif asc == False:
				# not safe report
				break
		elif cur < prev:
			if asc == None:
				asc = False
			elif asc == True:
				# not safe report
				break
		else:
			# not safe report
			break

		if cur > prev + 3 or cur < prev - 3:
			# not safe report
			break
	else:
		safe_reports += 1

print(safe_reports)