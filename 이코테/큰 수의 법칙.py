n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()

sum = 0
while True:
  if m >= k+1:
    sum += k * data[n-1] + data[n-2]
    m = m - k - 1
    continue
  else:
    for m in range(1,m):
      sum += data[n]
    break
print(sum)

#답지 풀이가 더 좋은듯..
#매 순간 확인하는 방식