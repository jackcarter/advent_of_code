def is_valid(passport):
	required_elements = ['byr',
					'iyr',
					'eyr',
					'hgt',
					'hcl',
					'ecl',
					'pid',
					#'cid',
					]

	passport_elements = passport.split(' ')
	passport_elements = [pe.split(':')[0] for pe in passport_elements]
	passport_elements.sort()
	print(passport_elements)
	for req_el in required_elements:
		if req_el not in passport_elements:
			return False
	return True

passports = []
with open("data.txt") as data:
	lines = data.read().splitlines()
lines.append('') #ensure we 'flush' the last passport to passports list

accumulator = []
for line in lines:
	if line != '':
		accumulator.append(line)
	else:
		passports.append(' '.join(accumulator))
		accumulator = []

num_valid = 0
for passport in passports:
	if is_valid(passport):
		print("valid")
		num_valid += 1

print(num_valid)

# Answer: 254