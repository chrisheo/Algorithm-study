n, k = map(int, input().split())

count = 0
#k로 최대한 나누면 횟수가 최소화가 된다
while n != 1:
  if n % k == 0:
    count += 1
    n = n / k
  else:
    count += 1
    n = n-1
print(count)