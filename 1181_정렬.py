from collections import defaultdict
import sys

l1 = []
d1 = defaultdict(list)
for i in range(int(input())):  
    l1.append(sys.stdin.readline().strip())

l1 = list(set(l1))
l1.sort()
num = len(l1)
for i in range(num):
    cnt = len(l1[i])
    d1[cnt].append(l1[i])
d1 = sorted(d1.items())
for i in d1:
    for j in i[1]:
        print(j)
