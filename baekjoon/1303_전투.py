import sys
from collections import deque

input = sys.stdin.readline


def bfs(x, y, c):
    cnt = 0
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if graph[nx][ny] == c and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    cnt += 1
    return cnt + 1


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
n, m = map(int, input().split())
graph = [list(input()) for _ in range(m)]
visited = [[False] * n for i in range(m)]
w , b = 0, 0
for i in range(m):
    for j in range(n):
        if graph[i][j] == 'W' and not visited[i][j]:
            w += bfs(i,j,'W') ** 2
        elif graph[i][j] == 'B' and not visited[i][j]:
            b += bfs(i, j, 'B') ** 2

print(w, b)