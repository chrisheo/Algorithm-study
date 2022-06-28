def main():
    #dfs
    N, M, K = map(int, input().split())
    response = dict()
    relationship = []
    visited = [0] * N
    for i in range(M):
        i,s = map(int, input().split())
        response[i] = s
    for i in range(K):
        ab = list(map(int, input().split()))
        relationship.append(ab)
    response = 0
    for i in range(N):
      response += getResponse(i)

def getResponse(i):
  if response[i] != null:
    return response[i]
  else:
    return getDFSResponse(i)

def getDFSResponse(i):
    return dfs(i,visited)
stack = []
def dfs(i, visited):
    visited[i] = 1
    for j in relationship:
      if i in relationship[j]:
        stack.append(j)




if __name__=="__main__":
    main()