import sys
N, M = input().split()
N = int(N)
M = int(M)
l = []
d = {}
for i in range(N):
    p = sys.stdin.readline().split()
    l.append(''.join(p))
    d[''.join(p)] = i + 1

for j in range(M):
    k = sys.stdin.readline().split()
    o = ''.join(k)
    if o.isdigit():
        o = int(o)
        print(l[o - 1])
    else:
        print(d[o])
