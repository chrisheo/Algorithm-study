import sys
import heapq
N = int(input())
cnt = 0
heap = []
for _ in range(N):
    n = sys.stdin.readline().strip()
    n = int(n)
    if n == 0:
        if cnt != 0:
            print(heapq.heappop(heap))
            cnt -= 1
        else:
            print(0)
    else:
        heapq.heappush(heap, n)
        cnt += 1
