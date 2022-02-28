from collections import deque
from sys import stdin
#45도 기울여서 보자
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

t = int(input()) 
count_list = []

def make_graph(m, n, k):
    graph = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, stdin.readline().split())
        graph[y][x] = 1
    return graph

def bfs(y, x):
    queue = deque([])
    queue.append([y, x])

    while queue:
        y, x = queue.pop()
        for d in range(4):
            xx = dx[d] + x
            yy = dy[d] + y
            if 0 <= xx < m and 0 <= yy < n:
                if graph[yy][xx] == 1:
                    graph[yy][xx] = 0
                    queue.append([yy, xx])


for _ in range(t):
    count = 0
    m, n, k = map(int, stdin.readline().split()) 
    graph = make_graph(m, n, k)
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(i, j)
                count += 1
    count_list.append(count)

print(*count_list, sep='\n')