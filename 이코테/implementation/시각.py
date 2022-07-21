N = int(input())
#0 <= N <= 23이고 60분, 60초 전체 중 3이 하나도 없는 가지수를 빼는 방향
count = 0
for h in range(N+1):
  if "3"  in str(h):
    count += 3600
  else:
    for m in range(60):
      for s in range(60):
        if "3"  in str(m) or "3"  in str(s):
          count +=1
print(count)