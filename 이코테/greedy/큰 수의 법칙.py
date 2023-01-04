n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()

# sum = 0
# while True:
#   if m >= k+1:
#     sum += k * data[n-1] + data[n-2]
#     m = m - k - 1
#     continue
#   else:
#     for m in range(1,m):
#       sum += data[n]
#     break
# print(sum)

# 답지 풀이가 더 좋은듯..
# 매 순간 확인하는 방식


# 수열 규칙을 이용한 방식

highest = data[-1]
second_highest = data[-2]
temp = m
result = 0

base = (m // (k + 1)) * k
base += (m % (k + 1))

result += highest * base
result += second_highest * (m - base)

print(result)
