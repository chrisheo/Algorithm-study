#파이썬 기본 정렬 알고리즘 이용
N = int(input())

array = []
for i in range(N):
  array.append(int(input()))

array.sort(reverse=True)
print(array)