from collections import deque

#DFS는 스택으로 구현할 수 있다.
def dfs(graph, v, visited):
  visited[v] = True
  print(v, end=' ')
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

#BFS는 큐를 활용해 구현할 수 있다.
def bfs(graph, v, visited):
  queue = deque([v])
  visited[v] = True
  while queue:
    e = queue.popleft()
    print(e, end=' ')
    for i in graph[e]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True
