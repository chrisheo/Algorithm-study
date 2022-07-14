#DFS 사용해보기
n, m = map(int, input().split())
tray = []
for i in range(n):
  line = list(map(int,input()))
  tray.append(line)

def dfs(x,y):
  if 0 <= x < n and 0 <= y < m:
    if tray[x][y] == True:
      return False
    else:
      tray[x][y] = 1
      dfs(x-1,y)
      dfs(x,y-1)
      dfs(x+1,y)
      dfs(x,y+1)
      return True
  else:
    return False

count = 0
for i in range(n):
  for j in range(m):
    if dfs(i,j) == True:
      count+= 1
print(count)