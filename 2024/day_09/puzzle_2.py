import math

with open("./data.txt") as data:
  lines = data.read().splitlines()

file_id = 0
is_file = True
aggregated = []
for c in lines[0]:
  if is_file:
    aggregated.append((file_id, int(c)))
    file_id += 1
  else:
    aggregated.append(('.', int(c)))
  is_file = not is_file

def print_agg(aggregated):
  for block in aggregated:
    for i in range(block[1]):
      print(block[0], end='')
  print()

i = len(aggregated) - 1
while i >= 0:
  if aggregated[i][0] == '.':
    i -= 1
    continue
  file_id, file_size = aggregated[i]
  for j in range(i):
    if aggregated[j][0] == '.':
      #check if we can fit the file
      if aggregated[j][1] == file_size:
        aggregated[j] = (file_id, file_size)
        aggregated[i] = ('.', file_size)
        break
      elif aggregated[j][1] > file_size:
        aggregated[i] = ('.', file_size) 
        aggregated.insert(j+1, ('.', aggregated[j][1] - file_size))
        aggregated[j] = (file_id, file_size)
        # check if we can merge empty space with next block
        if j+2 < len(aggregated) and aggregated[j+1][0] == '.' and aggregated[j+2][0] == '.':
          aggregated[j+1] = ('.', aggregated[j+1][1] + aggregated[j+2][1])
          aggregated[j+2] = ('.', 0)
        break
  i -= 1


score = 0
i = 0
for block in aggregated:
  if block[0] == '.':
    i += block[1]
    continue
  else:
    for n in range(block[1]):
      score += block[0]*i
      i+=1

print(score)