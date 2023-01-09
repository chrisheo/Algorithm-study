pers = int(input())
time = list(map(int, input().split()))
res = 0
time.sort()

for i in range(pers):
    res += time[i]*pers
    pers -=1

print(res)