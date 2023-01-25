from collections import deque

# dfs 알고리즘으로 최단 거리를 찾으려면 시간 복잡도가 커진다.
# bfs 알고리즘으로 최단 거리 보장 이용해보기

N, M = map(int, input().split())

miro = []

for _ in range(N):
    miro.append(list(input()))

miro[0][0] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = [[0, 0]]

# BFS 시작
while queue:
    x, y = queue[0][0], queue[0][1]

    del queue[0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if miro[nx][ny] == "1":
                queue.append([nx, ny])
                miro[nx][ny] = miro[x][y] + 1

print(miro[N - 1][M - 1])
