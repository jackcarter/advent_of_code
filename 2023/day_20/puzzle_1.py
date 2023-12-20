from math import inf
from copy import deepcopy
import re
import itertools

with open("./data.txt") as data:
	lines = data.read().splitlines()

modules = {}
for line in lines:
	a, b = line.split(' -> ')
	dests = b.split(', ')
	state = None
	if a == 'broadcaster':
		prefix = None
	else:
		prefix, a = a[0], a[1:]
		if prefix == '%':
			state = False
		elif prefix == '&':
			state = {}
	modules[a] = {"prefix": prefix, "dests": dests, "state": state}
for k, v in modules.items():
	if modules[k]['prefix'] == '&':
		#find all inputs
		inputs = [m for m in modules if k in modules[m]['dests']]
		modules[k]['state'] = {i: False for i in inputs}

#False = low, True = high
#False = off, True = on

start = modules['broadcaster']

def send_pulse(origin, destinations, high):
	pulses = []
	for dest in destinations:
		if dest not in modules:
			continue
		if modules[dest]['prefix'] == '%':
			if high:
				pass
			else:
				if modules[dest]['state']:
					modules[dest]['state'] = False
					pulses.append((dest, modules[dest]['dests'], False))
				else:
					modules[dest]['state'] = True
					pulses.append((dest, modules[dest]['dests'], True))
		elif modules[dest]['prefix'] == '&':
			modules[dest]['state'][origin] = high
			if all(modules[dest]['state'].values()):
				pulses.append((dest, modules[dest]['dests'], False))
			else:
				pulses.append((dest, modules[dest]['dests'], True))
		elif dest == 'broadcaster':
			pulses.append((dest, modules[dest]['dests'], high))
	return pulses

def count_pulses(next_pulses):
	return sum([len(pulse[1]) for pulse in next_pulses if pulse[2]]), sum([len(pulse[1]) for pulse in next_pulses if not pulse[2]])

def press_button():
	high = 0
	low = 0
	low += 1 #initial pulse
	pulses = send_pulse('button', ['broadcaster'], False)
	while len(pulses) > 0:
		h, l = count_pulses(pulses)
		high += h
		low += l
		next_pulses = deepcopy(pulses)
		pulses = []
		for pulse in next_pulses:
			pulses.extend(send_pulse(pulse[0], pulse[1], pulse[2]))
	return high, low

total_high = 0
total_low = 0
for i in range(1000):
	h, l = press_button()
	total_high += h
	total_low += l
print(total_high * total_low)