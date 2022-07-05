n, m = map(int, input().split())

array = []
#데이터를 입력받음과 동시에 로직 처리를 하는 습관 들이기
for i in range(n):
  data = list(map(int, input().split()))
  array.append(data)
local_max = 0

for i in range(n):
  min_num = min(array[i])
  local_max = max(min_num, local_max)
print(local_max)
