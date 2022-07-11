coordinates = input()
x = int(ord(coordinates[0]) - ord("a") + 1)
y = int(coordinates[1])

print(x,y)
steps = [(2,1), (-2,1), (-2,-1), (2,-1), (1,2), (1,-2), (-1,-2), (-1,2)]

count = 0
for i in steps:
  result_x = x + i[0]
  result_y = y + i[1]
  if 0 < int(result_x) < 9 and 0 < int(result_y) < 9:
    count += 1
  else:
    continue
print(count)