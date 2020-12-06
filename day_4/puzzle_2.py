import re

def hgt_valid(hgt):
	if hgt[-2:] == 'cm':
		return 150 <= int(hgt[:-2]) <= 193
	elif hgt[-2:] == 'in':
		return 59 <= int(hgt[:-2]) <= 76
	else:
		return False

def is_valid(passport):
	required_elements = {'byr': lambda x: 1920 <= int(x) <= 2002,
					'iyr': lambda x: 2010 <= int(x) <= 2020,
					'eyr': lambda x: 2020 <= int(x) <= 2030,
					'hgt': hgt_valid,
					'hcl': lambda x: re.match('^\#[a-f|\d]{6}$', x) is not None,
					'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
					'pid': lambda x: re.match('^\d{9}$', x) is not None,
					#'cid',
					}

	passport_elements = passport.split(' ')
	passport_elements = {pe.split(':')[0]: pe.split(':')[1] for pe in passport_elements}
	for req_el, test in required_elements.items():
		if req_el not in passport_elements.keys():
			return False
		elif test(passport_elements[req_el]) == False:
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
		num_valid += 1

print(num_valid)

# Answer: 184