from sys import stdin

n, k = map(int, stdin.readline().split())

values = []
for i in range(n):
    a = int(stdin.readline())
    values.append(a)

# 다음과 같은 방식도 존재
# values = [int(input()) for _ in range(n)]

answer = 0
values.sort(reverse=True)

for money in values:
    answer += k // money
    k %= money
    if k == 0:
        break
