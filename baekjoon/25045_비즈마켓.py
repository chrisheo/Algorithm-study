import sys

n,m = map(int, sys.stdin.readline().split())

satisfactions = [*map(int,input().split())]
costs = [*map(int,input().split())]

satisfactions.sort(reverse=True)
costs.sort()


sum = 0
for i in range(min(int(m),int(n))):
    if costs[i] > satisfactions[i]:
        break
    else:
        sum += int(satisfactions[i]) - int(costs[i])
print(sum)
