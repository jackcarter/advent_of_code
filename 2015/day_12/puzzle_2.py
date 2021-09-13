import re
import json

with open("data.txt") as data:
	text = data.read()

j = json.loads(text)

def sum_children(node):
	subtotal = 0
	# first, check if the node is a primitive
	if type(node) is int:
		subtotal = node
	elif type(node) is str:
		subtotal = 0
	else:
		# node is a dict or list. See if any property is 'red'
		try:
			for child in node:
				if node[child] == 'red':
					return 0
		except Exception as ex:
			pass
		# if no 'red' value found, continue parsing
		for child in node:
			if type(child) is int:
				subtotal += child
			elif type(child) is dict:
				subtotal += sum_children(child)
			elif type(child) is list:
				subtotal += sum_children(child)
			elif type(child) is str:
				try:
					subtotal += sum_children(node[child])
				except Exception as ex:
					pass
	return subtotal

print(sum_children(j))

# Answer: 111754